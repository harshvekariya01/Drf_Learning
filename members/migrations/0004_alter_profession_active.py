# Generated by Django 4.1.5 on 2023-02-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_profession_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]