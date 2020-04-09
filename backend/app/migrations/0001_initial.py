# Generated by Django 2.2.12 on 2020-04-09 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=20, null=True)),
                ('actors', models.CharField(blank=True, max_length=255, null=True)),
                ('awards', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('dvd', models.CharField(blank=True, max_length=20, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('plot', models.CharField(blank=True, max_length=500, null=True)),
                ('released', models.CharField(blank=True, max_length=20, null=True)),
                ('runtime', models.CharField(blank=True, max_length=20, null=True)),
                ('poster', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_movie', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
