from email.mime import image
from django.db import models


class HeadTeachers(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО завуча')
    image = models.ImageField(verbose_name='фото завуча', upload_to = 'product/%Y/%m/%d')
    phone = models.IntegerField(verbose_name='Номер телефона')

    def __str__(self) -> str:
        return f'Завуч: {self.name}'

    class Meta:
        verbose_name = 'Завуч'
        verbose_name_plural = 'Завучи'