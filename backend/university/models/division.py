from django.db import models
from django.db.models.signals import post_save
from .utils import *


class Division(models.Model):
    type = models.SmallIntegerField(verbose_name="Тип подразделения", default=0, choices=DIVISION_TYPE_CHOICES)
    title = models.CharField(max_length=150, unique=True, verbose_name="Название", blank=False)
    lead = models.OneToOneField("Staff", related_name="depend_division", verbose_name="Руководитель", null=True,
                             blank=True, on_delete=models.SET_NULL)

    head_depart = models.ForeignKey("Division", verbose_name="Головное подразделение", related_name="child_departs",
                                    blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.get_type_display()} {self.title}'

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"


def set_position(sender, instance, **kwargs):
    if instance.lead:

        if instance.type == RECTORATE_TYPE:
            instance.lead.position = RECTORATE_LEAD_POSITION
        elif instance.type == FACULTY_TYPE:
            instance.lead.position = FACULTY_LEAD_POSITION
        elif instance.type == CHAIN_TYPE:
            instance.lead.position = CHAIN_LEAD_POSITION

        instance.lead.division = instance
        instance.lead.save()


post_save.connect(set_position, sender=Division)
