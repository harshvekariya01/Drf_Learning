# Generated by Django 4.1.5 on 2023-02-22 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_remove_profession_profession_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='profession_no',
        ),
        migrations.AddField(
            model_name='profession',
            name='profession_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.student'),
        ),
    ]
