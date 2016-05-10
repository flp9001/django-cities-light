# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(null=True),
        ),
    ]
