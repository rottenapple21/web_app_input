# Generated by Django 3.1.2 on 2020-11-03 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app_input', '0002_auto_20201103_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='addlink',
            name='Pelajaran',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
