# Generated by Django 3.2.16 on 2023-03-31 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_coursespecification_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursespecification',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/course_photo', verbose_name='фото'),
        ),
    ]
