from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.db import models


'''class MyUserManager(BaseUserManager):

    def create_user(self, email, photo, password=None):

        user = self.model(
            email=self.normalize_email(email),
            photo=photo,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user'''


class User(AbstractUser):
    # add additional fields in here
    photo = models.ImageField(blank=True, null=True, upload_to='user/%Y/%m/%d')
    email = models.EmailField(unique=True)
    #REQUIRED_FIELDS = ["photo"]
    #objects = MyUserManager()

    def __str__(self):
        return self.username

