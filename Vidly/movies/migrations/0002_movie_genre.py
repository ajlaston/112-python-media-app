# Generated by Django 2.1 on 2019-11-29 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='movies.Genre'),
            preserve_default=False,
        ),
    ]
