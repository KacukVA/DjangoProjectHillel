# Generated by Django 4.1.2 on 2022-10-28 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_group_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
    ]
