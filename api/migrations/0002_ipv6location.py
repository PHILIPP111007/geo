# Generated by Django 4.2.3 on 2023-09-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPv6Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_first_integer', models.PositiveBigIntegerField()),
                ('ip_last_integer', models.PositiveBigIntegerField()),
                ('continent', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
                ('stateprov', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'IPv6 Location',
            },
        ),
    ]
