# Generated by Django 2.0.3 on 2018-04-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180415_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='commentary',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='objective',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='url',
            field=models.URLField(max_length=400),
        ),
    ]