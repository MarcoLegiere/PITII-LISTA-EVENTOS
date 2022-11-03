# Generated by Django 4.1 on 2022-08-31 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_meeting_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.CharField(blank=True, choices=[('p', 'Presencial'), ('o', 'Online')], default='p', help_text='Local Reunião', max_length=1),
        ),
    ]
