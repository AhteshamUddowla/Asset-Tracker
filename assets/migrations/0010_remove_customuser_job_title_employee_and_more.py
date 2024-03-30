# Generated by Django 4.0.4 on 2024-03-30 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0009_customuser_job_title_alter_asset_employee_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='job_title',
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=20, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assets.customuser')),
            ],
        ),
        migrations.AlterField(
            model_name='asset',
            name='employee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.employee'),
        ),
    ]
