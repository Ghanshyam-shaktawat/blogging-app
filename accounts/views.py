from multiprocessing import context
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm
from django.contrib import messages
from .models import CustomUser
from main.models import Post
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.tokens import account_active_token
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.models import User  
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        userform = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Bloggin Account'
            message = render_to_string('accounts/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_active_token.make_token(user),
            })
            user.email_user(subject, message)
            messages.success(request, ('Please Confirm your email to complete registration.'))
            return redirect('accounts:activate-mssg')
        
        return render(request, self.template_name, {'form': form})
            
class ActivationView(View):
    def get(self, request, token, *args, **kwargs):
        try : 
            uid = force_str(urlsafe_base64_decode(kwargs["uidb64"]))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            
        if user is not None and account_active_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, ('Your account has been confirmed.'))
            return redirect('main:index')
        else:
            messages.warning(request, ('The confirmation link was invalid, Possibly it is because it has been already activated.'))
            return redirect('main:index')
    
class ActivateMssgView(generic.TemplateView):
    template_name = 'accounts/activate.html'
    
    
class LoginView(auth_view.LoginView):
    form_class: LoginForm
    template_name= 'accounts/login.html'
    
class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/edit_profile.html'
    form_class = UserEditForm
    context_object_name = 'self_user'
    
    def get_object(self):
        return self.request.user
    
    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'username': self.get_context_data()['self_user'].username})
    
class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'main/profile.html'
    context_object_name='members'
    slug_field="username"
    slug_url_kwarg="username"
    
    def get_context_data(self, **kwargs):
        kwargs['user_post'] = self.object.posts.all()
        return super().get_context_data(**kwargs)