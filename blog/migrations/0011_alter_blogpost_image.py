# Generated by Django 4.0.6 on 2022-07-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/%Y/%m/%d'),
        ),
    ]
