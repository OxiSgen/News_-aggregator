# Generated by Django 3.2 on 2021-05-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0020_alter_news_same_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
