# Generated by Django 4.0 on 2021-12-22 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kashi', '0005_alter_kash_type_kash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kash',
            name='type_kash',
            field=models.CharField(choices=[('کاشی بزرگ', ' کاشی بزرگ'), ('کاشی کوچک', ' کاشی کوچک'), ('کاشی متوسط', ' کاشی متوسط')], default='drinks', max_length=10, verbose_name='نوع غذا'),
        ),
    ]
