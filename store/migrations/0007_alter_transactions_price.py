# Generated by Django 3.2 on 2021-04-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_cryptocurrency_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]