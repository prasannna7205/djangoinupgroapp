# Generated by Django 4.2.1 on 2023-08-23 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
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
        migrations.CreateModel(
            name='CollegeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Collegename', models.CharField(max_length=30)),
                ('CollegeHeading', models.TextField()),
                ('CollegeDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='host_UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institutionname', models.CharField(max_length=30)),
                ('InstitutionHeading', models.TextField()),
                ('InstitutionDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ourpartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PartnersNmae', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Schoolname', models.CharField(max_length=30)),
                ('SchoolHeading', models.TextField()),
                ('SchoolDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('category', models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('schoolpage', 'School Page')], max_length=20)),
                ('education_type', models.CharField(blank=True, choices=[('school', 'School'), ('college', 'College'), ('institute', 'Institute')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolPage',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inupgroapp.userprofile')),
                ('founder_name', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
            ],
            bases=('inupgroapp.userprofile',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inupgroapp.userprofile')),
                ('college_name', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
            ],
            bases=('inupgroapp.userprofile',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inupgroapp.userprofile')),
                ('school_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
            ],
            bases=('inupgroapp.userprofile',),
        ),
    ]
