# Generated by Django 4.2.1 on 2023-08-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inupgroapp', '0002_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='findjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postname', models.CharField(max_length=50)),
                ('fieldname', models.CharField(max_length=50)),
                ('officelocation', models.CharField(max_length=50)),
                ('minimumqualification', models.CharField(max_length=50)),
                ('experiencelavel', models.CharField(max_length=50)),
                ('vacancylocation', models.CharField(max_length=30)),
                ('jobdescription', models.TextField(max_length=100)),
                ('technicalrequirement', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
