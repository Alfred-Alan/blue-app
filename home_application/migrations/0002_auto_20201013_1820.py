# Generated by Django 2.2.6 on 2020-10-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosts',
            name='hostip',
            field=models.CharField(max_length=50, verbose_name='主机IP'),
        ),
    ]