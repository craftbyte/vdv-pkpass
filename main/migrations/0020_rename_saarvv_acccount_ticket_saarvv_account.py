# Generated by Django 5.0.9 on 2024-10-13 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_ticket_saarvv_acccount_alter_ticket_db_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='saarvv_acccount',
            new_name='saarvv_account',
        ),
    ]
