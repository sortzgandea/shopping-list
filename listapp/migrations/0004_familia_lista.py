# Generated by Django 3.0.6 on 2020-05-23 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listapp', '0003_auto_20200523_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='lista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listapp.Lista'),
        ),
    ]