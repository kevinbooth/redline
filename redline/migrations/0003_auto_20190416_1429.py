# Generated by Django 2.1.7 on 2019-04-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redline', '0002_auto_20190416_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
