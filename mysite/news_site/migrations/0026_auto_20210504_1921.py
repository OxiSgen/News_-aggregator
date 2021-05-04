# Generated by Django 3.2.1 on 2021-05-04 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_site', '0025_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlsForCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prior', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_site.category')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_site.urlstable')),
            ],
        ),
        migrations.RemoveField(
            model_name='priorityforuser',
            name='url',
        ),
        migrations.RemoveField(
            model_name='priorityforuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='urls',
        ),
        migrations.DeleteModel(
            name='CategoryForUser',
        ),
        migrations.DeleteModel(
            name='PriorityForUser',
        ),
        migrations.AddField(
            model_name='urlsforcategory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
