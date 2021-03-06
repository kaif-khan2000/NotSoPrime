# Generated by Django 3.0.8 on 2020-07-23 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200723_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='uploaded',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='seriesvideo',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Series'),
        ),
    ]
