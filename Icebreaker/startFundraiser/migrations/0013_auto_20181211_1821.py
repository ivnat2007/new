# Generated by Django 2.1.2 on 2018-12-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0012_auto_20181210_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
