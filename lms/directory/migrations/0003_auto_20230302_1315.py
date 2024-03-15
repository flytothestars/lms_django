# Generated by Django 3.2.16 on 2023-03-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_automationsystem_is_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='participationpurpose',
            name='is_other',
            field=models.BooleanField(default=False, verbose_name='другое'),
        ),
        migrations.AddField(
            model_name='problemortask',
            name='is_other',
            field=models.BooleanField(default=False, verbose_name='другое'),
        ),
    ]
