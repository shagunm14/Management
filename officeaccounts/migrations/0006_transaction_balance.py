# Generated by Django 2.2.4 on 2019-09-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officeaccounts', '0005_auto_20190903_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]