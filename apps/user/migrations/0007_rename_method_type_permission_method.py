# Generated by Django 5.0.3 on 2024-04-05 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_permission_method_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='method_type',
            new_name='method',
        ),
    ]