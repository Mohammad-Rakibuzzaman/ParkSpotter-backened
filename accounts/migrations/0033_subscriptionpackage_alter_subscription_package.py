# Generated by Django 4.2.13 on 2024-06-03 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_booking_is_paid_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration_months', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.AlterField(
            model_name='subscription',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.subscriptionpackage'),
        ),
    ]
