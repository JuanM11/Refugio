# Generated by Django 2.1.3 on 2018-11-24 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refugio', '0004_auto_20181124_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptante',
            name='mascota_a_adoptar',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]