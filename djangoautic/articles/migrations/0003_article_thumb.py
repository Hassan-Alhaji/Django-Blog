# Generated by Django 3.0.2 on 2020-11-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20201101_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='defult.png', upload_to=''),
        ),
    ]