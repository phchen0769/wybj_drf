# Generated by Django 5.0.3 on 2024-04-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_role_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='desc',
            field=models.CharField(help_text='描述', max_length=300, null=True, verbose_name='描述'),
        ),
    ]
