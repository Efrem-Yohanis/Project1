# Generated by Django 3.2.9 on 2022-11-10 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_remove_customer_order_adis_remove_customer_order_new_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_order',
            old_name='castel',
            new_name='Castle',
        ),
        migrations.RenameField(
            model_name='customer_order',
            old_name='doppel',
            new_name='Doppel',
        ),
        migrations.RenameField(
            model_name='customer_order',
            old_name='george',
            new_name='George',
        ),
        migrations.RenameField(
            model_name='customer_order',
            old_name='senq',
            new_name="Sen'q",
        ),
    ]
