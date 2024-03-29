# Generated by Django 4.1.5 on 2023-01-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Facebook profile link (non-obligatory)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Instagram profile link (non-obligatory)'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tiktok',
            field=models.URLField(blank=True, verbose_name='TikTok profile link (non-obligatory)'),
        ),
    ]
