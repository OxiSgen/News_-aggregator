# Generated by Django 3.2 on 2021-05-02 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0013_auto_20210502_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='SameNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_text', models.CharField(blank=True, max_length=200, null=True)),
                ('news_url', models.CharField(blank=True, max_length=200, null=True)),
                ('news_hype_rate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
                ('child_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_site.news')),
                ('site_url', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news_site.urlstable')),
            ],
        ),
    ]