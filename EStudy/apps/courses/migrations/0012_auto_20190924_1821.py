# Generated by Django 2.2.4 on 2019-09-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20190924_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(max_length=2000, verbose_name='访问地址'),
        ),
    ]