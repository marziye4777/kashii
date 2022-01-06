# Generated by Django 4.0 on 2021-12-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kashi', '0004_alter_kash_type_kash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kash',
            name='type_kash',
            field=models.CharField(choices=[('drinks', ' کاشی بزرگ'), ('dinner', ' کاشی کوچک'), ('lunch', ' کاشی متوسط')], default='drinks', max_length=10, verbose_name='نوع غذا'),
        ),
    ]