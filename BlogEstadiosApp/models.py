from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    description = models.TextField(blank=True)
    portfolio_link = models.URLField(blank=True)
    avatar = models.ImageField(
        upload_to='avatars/', default='default_avatar.jpg')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'


class Estadio(models.Model):
    name = models.CharField(max_length=200)
    apodo = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='estadiums_images/')

    def __str__(self):
        return self.title
