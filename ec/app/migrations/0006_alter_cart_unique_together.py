# Generated by Django 3.2.21 on 2023-11-10 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_cart_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set(),
        ),
    ]