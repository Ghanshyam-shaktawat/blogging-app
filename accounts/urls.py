from django.urls import path
from .views import ActivationView, LoginView, RegisterView, ActivateMssgView, UserUpdateView, UserProfileView
app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/', ActivateMssgView.as_view(), name='activate-mssg'),
    path('accounts/activate/<uidb64>/<token>/', ActivationView.as_view(), name='activate'),
    path('profile/edit/me/', UserUpdateView.as_view(), name='edit-profile'),
    path('profile/<slug:username>/', UserProfileView.as_view(), name='profile'),
]