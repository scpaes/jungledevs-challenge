from django.db import models
from .authors import Authors


class Articles(models.Model):
    author = models.ForeignKey(
        Authors, verbose_name='Author', related_name='Author', on_delete=models.CASCADE)
    category = models.CharField(blank=False, null=False, max_length=15)
    title = models.CharField(blank=False, null=False, max_length=15)
    summary = models.CharField(blank=False, null=False, max_length=32)

    class Meta:
        verbose_name = ('Artigo')
        verbose_name_plural = ('Artigos')

    def __str__(self) -> str:
        return self.title

