# Generated by Django 4.1.5 on 2023-01-25 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='school',
            field=models.CharField(default='XXX', max_length=3, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='School code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='code',
            field=models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='question13',
            field=models.IntegerField(choices=[(1, 'Mathematics/Physics'), (2, 'polski'), (3, 'Geography'), (4, 'IT'), (5, 'History/Society knowledge'), (6, 'Foreign Languages'), (7, 'Biology/Chemistry'), (8, 'PE')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)], verbose_name='My favorite subject at school is:'),
        ),
    ]
