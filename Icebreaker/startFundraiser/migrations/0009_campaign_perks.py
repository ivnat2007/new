# Generated by Django 2.1.2 on 2018-12-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0008_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='perks',
            field=models.BooleanField(default=False),
        ),
    ]
