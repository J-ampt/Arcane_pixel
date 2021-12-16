from collections import defaultdict
from django.db.models import (
    Model,
    CharField,
    EmailField,
    DateTimeField,
    SET_NULL,
    CASCADE,
)
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from autoslug import AutoSlugField


class User(AbstractUser):
    '''Defines the custom user model, with additional fields'''
    username = CharField(blank=False, null=False, unique=True, max_length=50)
    email = EmailField(blank=False, null=False, unique=True)
    slug = AutoSlugField(
        max_length=100, unique=True, blank=False, null=False,  populate_from='username',
    )

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
