# Generated by Django 4.2.1 on 2023-05-25 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]