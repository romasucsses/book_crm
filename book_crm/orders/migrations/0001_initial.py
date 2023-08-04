# Generated by Django 4.2.3 on 2023-07-26 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.IntegerField(default=30)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='pending', max_length=55)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_for_delivery', models.DateTimeField()),
                ('book', models.ManyToManyField(to='books.book')),
                ('customer_information', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client')),
            ],
        ),
    ]
