# Generated by Django 4.2.13 on 2024-05-12 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_booking_slot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='park_detail',
            new_name='park_detail_id',
        ),
        migrations.RenameField(
            model_name='park_detail',
            old_name='park_owner',
            new_name='park_owner_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='park_owner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='park_owner', to='accounts.parkowner'),
        ),
    ]