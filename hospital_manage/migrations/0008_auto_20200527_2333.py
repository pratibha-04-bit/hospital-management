# Generated by Django 2.0.5 on 2020-05-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_manage', '0007_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_form',
            name='available',
            field=models.CharField(choices=[('available', 'available'), ('not available', 'not available')], default='', max_length=20),
        ),
    ]