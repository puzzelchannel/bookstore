# Generated by Django 4.1.4 on 2022-12-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_comment_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='recomend',
            field=models.BooleanField(default=True),
        ),
    ]
