# Generated by Django 2.1.2 on 2018-12-06 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0005_auto_20181207_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
