# Generated by Django 4.2.7 on 2023-11-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_gamestats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gamestats',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]