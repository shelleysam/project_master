# Generated by Django 3.2.5 on 2021-08-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='appModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='employeeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('eid', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('pswd', models.CharField(max_length=10000000000)),
            ],
        ),
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=200)),
                ('index', models.CharField(max_length=10000000000)),
            ],
        ),
        migrations.CreateModel(
            name='formsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('pdf', models.FileField(upload_to='pdfs/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='rejectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
                ('reas', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='sec_accpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
                ('coll_d', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='sec_appModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='temp1Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='temp2Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='tempModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='test1Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=800)),
                ('pdf', models.CharField(max_length=10000)),
            ],
        ),
    ]
