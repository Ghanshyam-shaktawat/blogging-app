from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class RegistrationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp: int):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + 
            six.text_type(user.is_active)
        )
        
account_active_token = RegistrationTokenGenerator()