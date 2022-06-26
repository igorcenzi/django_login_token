from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError('Email precisa ser enviado.')
    
    email = self.normalize_email(email)
    
    user = self.model(
      email = email,
      **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user