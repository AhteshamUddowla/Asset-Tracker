# Generated by Django 4.0.4 on 2024-03-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(choices=[('Phone', 'Phone'), ('Tablet', 'Tablet'), ('Laptop', 'Laptop'), ('PC', 'PC')], max_length=20)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('assigned_date', models.DateField(blank=True, null=True)),
                ('returned_date', models.DateField(blank=True, null=True)),
                ('assigned_condition', models.CharField(blank=True, max_length=100, null=True)),
                ('returned_condition', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]