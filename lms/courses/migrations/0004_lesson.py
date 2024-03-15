# Generated by Django 3.2.16 on 2023-02-27 06:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Идентификатор')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено ли?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('created_by_id', models.UUIDField(null=True, verbose_name='Создатель')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('updated_by_id', models.UUIDField(null=True, verbose_name='Кто изменил')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', related_query_name='lesson', to='courses.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'занятие',
                'verbose_name_plural': 'занятия',
                'db_table': 'courses_lesson',
                'ordering': ['created_at'],
            },
        ),
    ]
