# Generated by Django 2.0.5 on 2018-12-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0010_auto_20181202_0119'),
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
