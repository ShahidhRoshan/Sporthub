from django.db import models
from django.db.models.base import Model



# Create your models here.



class tbl_turf(models.Model):
    turf_id=models.CharField(max_length=90)
    turf_name=models.CharField(max_length=90)
    contact_no=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    working_hrs=models.CharField(max_length=90)
    location=models.CharField(max_length=90)
    fee=models.CharField(max_length=90)
    photo=models.ImageField( upload_to="media", null=True, blank=True)
    status=models.CharField(max_length=90)

    class Meta:
        db_table="tbl_turf"

