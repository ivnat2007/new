# Generated by Django 2.0.5 on 2018-12-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0012_auto_20181202_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(null=True, to='marketplace.product'),
        ),
    ]
