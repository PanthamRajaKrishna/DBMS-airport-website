# Generated by Django 4.2.4 on 2023-11-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Confirmed', 'Confirmed')], max_length=45),
        ),
    ]
