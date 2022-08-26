from django.db import models


class Call(models.Model):
    crime_id = models.CharField(max_length=255)
    original_crime_type_name = models.CharField(max_length=255)
    report_date = models.DateTimeField(null=True, blank=False)
    call_date = models.DateTimeField(null=True, blank=False)
    offense_date = models.DateTimeField(null=True, blank=False)
    call_time = models.TimeField(null=True, blank=False)
    call_date_time = models.DateTimeField(null=True, blank=False)
    disposition = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255)
    common_location = models.CharField(max_length=255, default='')
