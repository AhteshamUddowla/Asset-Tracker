# Generated by Django 4.0.4 on 2024-03-29 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_asset_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.company'),
        ),
    ]
