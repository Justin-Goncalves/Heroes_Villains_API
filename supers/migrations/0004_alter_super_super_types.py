# Generated by Django 4.0.3 on 2022-03-18 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0002_rename_super_types_supertype'),
        ('supers', '0003_rename_seconday_ability_super_secondary_ability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super',
            name='super_types',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
        ),
    ]
