# Generated by Django 4.0.1 on 2022-02-08 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('englishmap', '0004_comment_timestamp_alter_comment_name_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='body',
            new_name='bodyR',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='name',
            new_name='nameR',
        ),
    ]