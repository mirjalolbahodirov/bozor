# Generated by Django 2.0 on 2017-12-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20171206_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(default='', max_length=200),
        ),
    ]
