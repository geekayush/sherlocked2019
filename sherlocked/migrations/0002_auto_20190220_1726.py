# Generated by Django 2.1.5 on 2019-02-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sherlocked', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
