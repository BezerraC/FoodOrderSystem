# Generated by Django 2.2.7 on 2023-03-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20230307_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='table',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]