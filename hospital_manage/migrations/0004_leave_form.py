# Generated by Django 2.0.5 on 2020-05-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_manage', '0003_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_no', models.CharField(max_length=50)),
                ('doctor_name', models.CharField(max_length=70)),
                ('department', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'leave_form',
            },
        ),
    ]
