# Generated by Django 4.1 on 2022-09-22 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nome')),
                ('password', models.CharField(max_length=50, verbose_name='Senha')),
                ('email', models.EmailField(max_length=120, verbose_name='E-mail')),
            ],
            options={
                'ordering': ['name', 'email'],
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigIntegerField(default=uuid.uuid4, help_text='ID UNICO', primary_key=True, serialize=False)),
                ('name_meeting', models.CharField(max_length=120, verbose_name='Nome da reunião')),
                ('date_meeting', models.DateField(verbose_name='Data da reunião')),
                ('link', models.CharField(blank=True, max_length=400, verbose_name='Link da reunião')),
                ('public', models.CharField(choices=[('p', 'Publicado'), ('a', 'Arquivado')], default='p', help_text='Publicar ou Arquivar', max_length=1)),
                ('local', models.CharField(choices=[('p', 'Presencial'), ('o', 'Online')], default='p', help_text='Local Reunião', max_length=1)),
                ('status', models.CharField(choices=[('p', 'Público'), ('f', 'Fechado')], default='f', help_text='Status da reunião', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('matricula', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=120)),
                ('setor', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.meeting')),
            ],
        ),
    ]
