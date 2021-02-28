# Generated by Django 3.1.3 on 2021-01-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=200)),
                ('lastName', models.CharField(blank=True, max_length=200)),
                ('stream', models.CharField(blank=True, max_length=200)),
                ('course', models.CharField(blank=True, max_length=200)),
                ('year', models.CharField(blank=True, max_length=200)),
                ('position', models.CharField(blank=True, max_length=200)),
                ('deptName', models.CharField(blank=True, max_length=200)),
                ('quote', models.TextField(blank=True, max_length=400)),
                ('posnum', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
