# Generated by Django 4.0.1 on 2022-02-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short',
            field=models.TextField(default='no descr'),
            preserve_default=False,
        ),
    ]