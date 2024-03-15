# Generated by Django 3.2.16 on 2023-03-02 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20230302_1315'),
        ('enrollees', '0002_enrollee_listener'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempenrollee',
            name='another_participation_purpose',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Цель Вашего участия в Программе обучения «Almaty Business 2023»'),
        ),
        migrations.AlterField(
            model_name='tempenrollee',
            name='description',
            field=models.TextField(verbose_name='Опишите, чем именно занимается Ваша компания'),
        ),
        migrations.AlterField(
            model_name='tempenrollee',
            name='is_recording_average_check',
            field=models.BooleanField(default=False, verbose_name='Ведете ли Вы учет среднего чека на 1 клиента'),
        ),
        migrations.AlterField(
            model_name='tempenrollee',
            name='is_recording_customers',
            field=models.BooleanField(default=False, verbose_name='Ведете ли Вы учет клиентов Вашего бизнеса'),
        ),
        migrations.AlterField(
            model_name='tempenrollee',
            name='is_used_automation',
            field=models.BooleanField(default=False, verbose_name='Применяете ли Вы автоматизацию в своей деятельности.'),
        ),
        migrations.AlterField(
            model_name='tempenrollee',
            name='lang',
            field=models.CharField(choices=[('KK', 'Қазақ тілі'), ('RU', 'Русский язык')], default='RU', max_length=50, verbose_name='На каком языке Вы хотите пройти обучение'),
        ),
        migrations.AlterField(
            model_name='tempenrollee',
            name='participation_purpose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temp_enrollees', related_query_name='temp_enrollee', to='directory.participationpurpose', verbose_name='Цель Вашего участия в Программе обучения «Almaty Business 2023»'),
        ),
        migrations.AlterField(
            model_name='tempenrollee',
            name='problem_or_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='temp_enrollees', related_query_name='temp_enrollee', to='directory.problemortask', verbose_name='Определите проблемы или задачи бизнеса, которые Вы хотели бы решить в рамках программы обучения'),
        ),
    ]
