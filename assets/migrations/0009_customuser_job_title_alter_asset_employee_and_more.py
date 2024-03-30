# Generated by Django 4.0.4 on 2024-03-30 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0008_asset_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='job_title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='employee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.customuser'),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
