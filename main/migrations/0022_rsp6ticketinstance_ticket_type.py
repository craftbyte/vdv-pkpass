# Generated by Django 5.0.9 on 2024-11-17 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0021_alter_ticket_ticket_type_rsp6ticketinstance"),
    ]

    operations = [
        migrations.AddField(
            model_name="rsp6ticketinstance",
            name="ticket_type",
            field=models.PositiveIntegerField(default=6),
        ),
    ]
