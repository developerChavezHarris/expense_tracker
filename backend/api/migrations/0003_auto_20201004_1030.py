# Generated by Django 3.1.1 on 2020-10-04 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201004_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expensemodel',
            old_name='name',
            new_name='expense',
        ),
    ]
