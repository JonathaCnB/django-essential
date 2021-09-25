# Generated by Django 3.2.6 on 2021-09-23 01:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajax_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webseries',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webseries',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webseries',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]