# Generated by Django 4.1.1 on 2022-09-09 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='inventoryItems',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('inventoryItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.order')),
            ],
        ),
    ]
