# Generated by Django 4.0.2 on 2022-02-22 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0004_chatthread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatthread',
            name='second_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
