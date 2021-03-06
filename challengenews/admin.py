from django.contrib import admin
from challengenews.models import *


class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = [
        'author',
        'category',
        'title',
        'slug'
    ]
    list_display_links = [
        'author',
        'category',
        'title',
        'slug'
    ]
    search_fields = ['author', 'title']


class AuthorsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
    list_display_links = [
        'name',
    ]
    search_fields = ['name', ]


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Authors, AuthorsAdmin)
