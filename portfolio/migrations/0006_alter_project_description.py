# Generated by Django 4.2.7 on 2023-11-27 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
