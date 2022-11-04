# Generated by Django 4.1 on 2022-09-02 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0022_meeting_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='link',
            field=models.CharField(blank=True, max_length=400, verbose_name='Link da reunião'),
        ),
    ]