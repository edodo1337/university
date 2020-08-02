# Generated by Django 2.2.14 on 2020-08-02 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(0, '----'), (1, 'Ректорат'), (2, 'Факультет'), (3, 'Кафедра')], default=0, verbose_name='Тип подразделения')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('head_depart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_departs', to='university.Division', verbose_name='Головное подразделение')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=150, verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('photo', models.ImageField(blank=True, upload_to='staff/photo/', verbose_name='Фото')),
                ('position', models.SmallIntegerField(choices=[(0, '----'), (6, 'Ректор'), (7, 'Проректор по науке'), (8, 'Проректор по образованию'), (9, 'Проректор по экономике'), (1, 'Декан'), (2, 'Заведующий кафедрой'), (3, 'Профессор'), (4, 'Доцент'), (5, 'Преподаватель')], default=0, verbose_name='Должность')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff', to='university.Division', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.AddField(
            model_name='division',
            name='lead',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='depend_division', to='university.Staff', verbose_name='Руководитель'),
        ),
    ]