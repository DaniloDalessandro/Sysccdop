from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


#===============================================================================

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


#===============================================================================

class User(AbstractBaseUser):
    avatar = models.TextField(default="/media/avatars/default-avatar.png")
    name = models.CharField(max_length=80,verbose_name="Nome")
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    is_superuser = models.BooleanField(default=False, verbose_name="Superusuário")
    last_access = models.DateTimeField(auto_now_add=True, verbose_name="Último acesso")

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        db_table = "users"