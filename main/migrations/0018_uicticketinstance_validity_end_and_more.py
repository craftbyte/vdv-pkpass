# Generated by Django 5.0.9 on 2024-10-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_dbsubscription_options_ticket_db_subscription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uicticketinstance',
            name='validity_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uicticketinstance',
            name='validity_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
