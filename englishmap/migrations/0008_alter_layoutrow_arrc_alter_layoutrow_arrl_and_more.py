# Generated by Django 4.0.1 on 2022-02-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishmap', '0007_layoutrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layoutrow',
            name='arrC',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='layoutrow',
            name='arrL',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='layoutrow',
            name='arrR',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='layoutrow',
            name='topC',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='layoutrow',
            name='topL',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='layoutrow',
            name='topR',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
