from . import *
from django.db import models
from .authors import Authors


class Articles(models.Model):
    id = models.CharField(primary_key=True, default=gen_uuid, max_length=36)
    author = models.ForeignKey(
        Authors, verbose_name='Author', related_name='Author', on_delete=models.CASCADE)
    category = models.CharField(blank=False, null=False, max_length=15)
    title = models.CharField(blank=False, null=False, max_length=15)
    summary = models.CharField(blank=False, null=False, max_length=32)
    first_paragraph = models.CharField(max_length=64, blank=False, null=False, default='')


    class Meta:
        verbose_name = ('Artigo')
        verbose_name_plural = ('Artigos')

    def __str__(self) -> str:
        return self.title
