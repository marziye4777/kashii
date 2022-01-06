# Generated by Django 4.0 on 2021-12-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kashi', '0003_kash_type_kash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kash',
            name='type_kash',
            field=models.CharField(choices=[('b', ' کاشی بزرگ'), ('k', ' کاشی کوچک'), ('m', ' کاشی متوسط')], default='m', max_length=10, verbose_name='نوع غذا'),
        ),
    ]