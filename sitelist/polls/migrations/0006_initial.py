# Generated by Django 4.1 on 2022-08-31 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polls', '0005_remove_meeting_author_delete_user_delete_meeting_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_meeting', models.CharField(max_length=120, verbose_name='Nome da reunião')),
                ('date_meeting', models.DateField(verbose_name='Data da reunião')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nome')),
                ('password', models.CharField(max_length=50, verbose_name='Senha')),
                ('email', models.CharField(max_length=120, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=120)),
                ('setor', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.meeting', verbose_name='Nome da Reunião')),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.owner', verbose_name='Autor'),
        ),
    ]