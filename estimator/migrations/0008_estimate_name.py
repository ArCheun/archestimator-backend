# Generated by Django 2.2.2 on 2019-07-07 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimator', '0007_phase_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='name',
            field=models.CharField(default="Amila's Estimate for Enterprise 6.5 - LDAP for Mobile", max_length=1000),
            preserve_default=False,
        ),
    ]
