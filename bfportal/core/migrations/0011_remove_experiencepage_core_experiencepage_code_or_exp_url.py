# Generated by Django 3.2.11 on 2022-01-17 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220117_2339'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='experiencepage',
            name='core_experiencepage_code_or_exp_url',
        ),
    ]
