# Generated by Django 2.0.5 on 2018-12-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_user', models.CharField(default='', max_length=30)),
                ('otp', models.CharField(default='', max_length=6)),
                ('num', models.IntegerField(default=0, max_length=1)),
            ],
        ),
    ]