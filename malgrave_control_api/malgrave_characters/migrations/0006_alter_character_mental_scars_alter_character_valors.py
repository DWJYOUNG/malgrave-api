# Generated by Django 5.0.3 on 2024-03-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malgrave_characters', '0005_alter_character_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='mental_scars',
            field=models.CharField(default='empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='character',
            name='valors',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]
