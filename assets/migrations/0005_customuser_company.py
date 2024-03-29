# Generated by Django 4.0.4 on 2024-03-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_asset_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.company'),
        ),
    ]
