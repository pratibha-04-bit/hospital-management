# Generated by Django 2.0.5 on 2020-05-14 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_no', models.CharField(max_length=50)),
                ('doc_name', models.CharField(max_length=70)),
                ('doc_phone', models.IntegerField()),
                ('doc_email', models.EmailField(max_length=50)),
                ('department_id', models.IntegerField()),
                ('doj', models.DateField()),
                ('gender', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
    ]