# Generated by Django 4.2.3 on 2023-10-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]