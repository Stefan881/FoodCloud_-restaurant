# Generated by Django 5.0.2 on 2024-03-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restraurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='assets/images'),
        ),
    ]
