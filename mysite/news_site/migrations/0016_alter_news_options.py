# Generated by Django 3.2 on 2021-05-02 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0015_auto_20210502_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['pub_date']},
        ),
    ]
