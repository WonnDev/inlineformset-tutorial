# Generated by Django 3.2.15 on 2022-10-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'fornecedor',
                'verbose_name_plural': 'fornecedores',
            },
        ),
    ]
