from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth.models import User
from django.db.models.base import Model

class CaseInsensitiveModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, default=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field: username})

        except UserModel.DoesNotExist:
            UserModel().set_password(password)

        else: 
            if user.check_password(password) and self.user_can_authenticate(user):
                return user