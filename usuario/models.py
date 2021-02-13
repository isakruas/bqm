from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models
from rest_framework.authtoken.models import Token


class Base(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Os usuários devem ter um endereço de email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)

        return user.id

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)

        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Não foi possivel definir como super usuario')

        return self.create_user(email, password, **extra_fields)

    class Meta:
        abstract = True


class Usuario(AbstractBaseUser, PermissionsMixin):
    objects = Base()

    nome = models.CharField(
        max_length=30,
        blank=None
    )

    sobrenome = models.CharField(
        max_length=30,
        blank=None

    )

    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,

    )

    escolaridade = models.CharField(
        verbose_name='Escolaridade',
        max_length=255,
        blank=None
    )

    nivel_de_acesso = models.CharField(
        max_length=10,
        default='epsilon',
        blank=None
    )

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'escolaridade', 'nivel_de_acesso']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_superuser

    @property
    def is_admin(self):
        # Simplest possible answer: All admins are staff
        return self.is_superuser


class Filiacao(models.Model):
    superior = models.IntegerField(
        null=False,
        blank=False,
    )

    inferior = models.IntegerField(
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Filiação'
        verbose_name_plural = 'Filiações'
        ordering = ['id']
