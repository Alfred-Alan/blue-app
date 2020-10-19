# Generated by Django 2.2.6 on 2020-10-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, verbose_name='主机名称')),
                ('hostip', models.TextField(verbose_name='主机IP')),
            ],
            options={
                'verbose_name': '主机表',
                'verbose_name_plural': '主机表',
                'db_table': 'Hosts',
            },
        ),
        migrations.CreateModel(
            name='Scripts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scriptname', models.CharField(max_length=50, verbose_name='脚本名称')),
                ('scriptcontent', models.TextField(verbose_name='脚本内容')),
            ],
            options={
                'verbose_name': '脚本表',
                'verbose_name_plural': '脚本表',
                'db_table': 'Scripts',
            },
        ),
    ]
