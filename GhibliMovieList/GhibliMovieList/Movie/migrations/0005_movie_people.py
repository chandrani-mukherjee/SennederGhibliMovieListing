# Generated by Django 3.1.3 on 2020-11-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieCharacter', '0002_auto_20201107_1537'),
        ('Movie', '0004_auto_20201107_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='people',
            field=models.ManyToManyField(to='MovieCharacter.People'),
        ),
    ]