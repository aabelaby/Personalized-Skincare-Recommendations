# Generated by Django 5.1.5 on 2025-02-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_productskintype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_skintype', models.CharField(max_length=30)),
            ],
        ),
    ]
