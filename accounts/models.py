from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,reg,full_name=None,password=None,is_staff=False,is_admin=False,is_active=True):
        if not reg:
            raise ValueError("Users must have a matriculation number!")
        if not password:
            raise ValueError("Users must have a password!")
        user_obj = self.model(
            reg = reg,
            full_name = full_name,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staff_user(self,reg,full_name=None,password=None):
        user = self.create_user(
            reg=reg,
            full_name=full_name,
            password=password,
            is_staff=True

        )

        return user
    
    def create_superuser(self,reg,full_name=None,password=None):
        user = self.create_user(
            reg=reg,
            full_name=full_name,
            password=password,
            is_admin=True,
            is_staff=True,

        )

        return user

class CustomUser(AbstractBaseUser):
    reg = models.CharField(max_length=15,unique=True)
    full_name = models.CharField(max_length=255,null=True,blank=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'reg'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.reg
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active