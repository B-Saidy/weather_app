# Generated by Django 2.2.4 on 2020-06-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='media/photos')),
                ('content', models.TextField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
    ]
