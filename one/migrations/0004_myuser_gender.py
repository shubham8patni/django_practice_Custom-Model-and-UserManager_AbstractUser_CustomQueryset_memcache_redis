# Generated by Django 4.1.2 on 2022-10-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_alter_myuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10, null=True),
        ),
    ]
