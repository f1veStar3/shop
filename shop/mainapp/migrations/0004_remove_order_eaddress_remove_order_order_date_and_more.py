# Generated by Django 4.2 on 2023-05-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_delete_startphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='eaddress',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.AddField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('self', 'Нова Пошта'), ('delivery', 'Укрпошта')], default='self', max_length=100, verbose_name='Пошта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='number_nova_post',
            field=models.CharField(max_length=111, verbose_name='віділення пошти'),
        ),
    ]