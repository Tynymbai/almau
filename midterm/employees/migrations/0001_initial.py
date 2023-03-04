# Generated by Django 4.1.7 on 2023-03-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='full_name')),
                ('position', models.CharField(max_length=255, verbose_name='position')),
                ['salary', models.IntegerField(max_length=100, verbose_name='salary')],
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
            },
        ),
    ]
