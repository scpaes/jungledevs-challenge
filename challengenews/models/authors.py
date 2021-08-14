from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Autor'

    def __str__(self) -> str:
        return self.name
