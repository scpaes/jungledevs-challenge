from . import *
from django.db import models
from django.utils.text import slugify
from .authors import Authors


class Articles(models.Model):
    id = models.CharField(primary_key=True, default=gen_uuid, max_length=36)
    author = models.ForeignKey(
        Authors, verbose_name='Author', related_name='Author', on_delete=models.CASCADE)
    category = models.CharField(blank=False, null=False, max_length=15)
    title = models.CharField(blank=False, null=False, max_length=15)
    summary = models.CharField(blank=False, null=False, max_length=32)
    first_paragraph = models.CharField(max_length=64, blank=False, null=False, default='')
    body = models.CharField(max_length=64, blank=False, null=False, default='')
    
    slug = models.SlugField(max_length=30, default='', verbose_name='title-slug')

    class Meta:
        verbose_name = ('Artigo')
        verbose_name_plural = ('Artigos')

    def __str__(self) -> str:
        return self.title

    def save(self, force_insert=True, using=None) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(force_insert=force_insert, using=using)
