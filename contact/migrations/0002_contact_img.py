# Generated by Django 5.0 on 2024-01-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='contact/'),
        ),
    ]