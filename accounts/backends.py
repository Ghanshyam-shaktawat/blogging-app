from asyncio import InvalidStateError
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib import messages 
from django.forms import ValidationError

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username: None, password: None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            return None
            # raise ValidationError(("The username/email or password is incorrect. Please check again!"),
            #     code='inactive',
            # )
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username))
            
        if user.check_password(password) and self.user_can_authenticate(user):
            return user