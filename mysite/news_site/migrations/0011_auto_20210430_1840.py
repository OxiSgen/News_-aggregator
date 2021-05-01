# Generated by Django 3.2 on 2021-04-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0010_remove_customuser_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='site_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]