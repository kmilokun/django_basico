# Generated by Django 4.0.6 on 2022-07-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_director_die'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='die',
            field=models.DateField(blank=True, null=True),
        ),
    ]
