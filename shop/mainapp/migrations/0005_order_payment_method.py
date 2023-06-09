# Generated by Django 4.2 on 2023-05-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_order_eaddress_remove_order_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('pay_on_delivery', 'Оплата на пошті'), ('online_payment', 'Онлайн-оплата')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
