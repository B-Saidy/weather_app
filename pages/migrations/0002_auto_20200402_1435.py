# Generated by Django 2.2.4 on 2020-04-02 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]