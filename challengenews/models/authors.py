from . import *
from django.db import models


class Authors(models.Model):
    id = models.CharField(primary_key=True, default=gen_uuid, max_length=36)
    name = models.CharField(max_length=32)
    picture = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Autor'

    def __str__(self) -> str:
        return self.name
