# Generated by Django 4.2.3 on 2023-10-02 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_employee_work_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='onBoardDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]