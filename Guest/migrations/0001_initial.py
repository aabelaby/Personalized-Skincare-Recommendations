# Generated by Django 5.1.5 on 2025-02-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=50)),
                ('user_age', models.CharField(max_length=50)),
                ('user_gender', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
    ]
