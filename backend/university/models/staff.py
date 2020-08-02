from django.db import models
from university.models.utils import *


class Staff(models.Model):
    first_name = models.CharField(max_length=150, blank=False, verbose_name="Имя")
    last_name = models.CharField(max_length=150, blank=False, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, blank=False, verbose_name="Отчество")
    birthday = models.DateField(verbose_name="День рождения")
    photo = models.ImageField(blank=True, verbose_name="Фото", upload_to="staff/photo/")

    division = models.ForeignKey("Division", related_name="staff", verbose_name="Подразделение", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    position = models.SmallIntegerField(blank=False, verbose_name="Должность", default=0, choices=POSITION_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    def __repr__(self):
        return f'{self.last_name} {self.first_name[0]}.{self.patronymic[0]}.'

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
