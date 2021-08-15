# Generated by Django 3.2.6 on 2021-08-15 02:01

import challengenews.models.articles
import challengenews.models.authors
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challengenews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.CharField(default=challengenews.models.articles.gen_uuid, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='authors',
            name='id',
            field=models.CharField(default=challengenews.models.authors.gen_uuid, max_length=36, primary_key=True, serialize=False),
        ),
    ]