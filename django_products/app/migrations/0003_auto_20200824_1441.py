# Generated by Django 3.1 on 2020-08-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliverDate',
            field=models.DateTimeField(null=True),
        ),
    ]
