# Generated by Django 5.0.1 on 2024-02-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_smsverifycode_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='角色'),
        ),
    ]
