# Generated by Django 2.2.4 on 2019-09-27 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20190927_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
                ('course_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='courses.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=('courses.course',),
        ),
    ]
