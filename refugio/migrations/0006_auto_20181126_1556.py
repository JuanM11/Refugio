# Generated by Django 2.1.2 on 2018-11-26 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugio', '0005_auto_20181126_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(upload_to='fotos'),
        ),
    ]