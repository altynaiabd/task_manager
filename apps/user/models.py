from django.db import models


class UserModel(models.Model):
    username = models.CharField(verbose_name='Имя пользователя', max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username