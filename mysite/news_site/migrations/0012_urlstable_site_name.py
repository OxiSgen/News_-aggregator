# Generated by Django 3.2 on 2021-05-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0011_auto_20210430_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlstable',
            name='site_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
