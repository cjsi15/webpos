# Generated by Django 4.1.3 on 2022-12-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('barcode', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.FloatField(verbose_name=2)),
                ('retail', models.FloatField(verbose_name=2)),
            ],
        ),
    ]