# Generated by Django 4.1 on 2022-08-31 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_meeting_author_alter_meeting_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='author',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Meeting',
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
