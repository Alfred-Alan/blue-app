# Generated by Django 2.2.6 on 2020-10-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0005_apps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='server',
            field=models.IntegerField(verbose_name='隶属服务器'),
        ),
    ]