# Generated by Django 4.2.3 on 2023-09-02 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_ip_first_integer_ipv4location_ip_first_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipv4location',
            options={'ordering': ['ip_first', 'ip_last'], 'verbose_name': 'IPv4 Location'},
        ),
    ]