# Generated by Django 4.1.5 on 2023-02-22 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_remove_profession_profession_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='profession_no',
        ),
        migrations.AddField(
            model_name='profession',
            name='profession_no',
            field=models.ManyToManyField(blank=True, null=True, to='members.student'),
        ),
    ]
