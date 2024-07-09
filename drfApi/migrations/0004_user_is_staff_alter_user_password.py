# Generated by Django 5.0.6 on 2024-07-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfApi', '0003_user_tasks_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
