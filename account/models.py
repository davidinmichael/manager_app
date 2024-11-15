from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from core.models import BaseModel



class AccountManager(BaseUserManager):
	pass

class Account(AbstractUser, BaseModel):
	pass
