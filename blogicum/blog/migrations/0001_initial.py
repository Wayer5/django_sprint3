# Generated by Django 3.2.16 on 2023-10-14 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(verbose_name='Слаг')),
                ('is_published', models.BooleanField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('is_published', models.BooleanField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'место',
                'verbose_name_plural': 'Место',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('pub_date', models.DateTimeField()),
                ('is_published', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('output_order', models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.location')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'Пост',
            },
        ),
    ]
