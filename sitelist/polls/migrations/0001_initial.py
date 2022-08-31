# Generated by Django 4.1 on 2022-08-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Confirm',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_meeting', models.CharField(max_length=120)),
                ('matricula', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=120)),
                ('setor', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='meeting',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name_meeting', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=80)),
                ('date_meeting', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=120)),
            ],
        ),
    ]