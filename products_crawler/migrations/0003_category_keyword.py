# Generated by Django 2.0.3 on 2018-05-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_crawler', '0002_auto_20180516_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='keyword',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
