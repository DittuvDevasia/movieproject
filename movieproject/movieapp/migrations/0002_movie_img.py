# Generated by Django 3.2.14 on 2022-08-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfdff', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
