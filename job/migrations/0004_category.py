# Generated by Django 4.1.7 on 2023-03-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_salaey_job_salay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
