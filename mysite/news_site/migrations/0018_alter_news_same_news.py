# Generated by Django 3.2 on 2021-05-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0017_alter_news_same_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='same_news',
            field=models.ManyToManyField(related_name='_news_site_news_same_news_+', to='news_site.News', verbose_name='Same News'),
        ),
    ]
