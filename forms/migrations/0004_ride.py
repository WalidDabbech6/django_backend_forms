# Generated by Django 4.2.10 on 2024-02-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20231121_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
            ],
        ),
    ]
