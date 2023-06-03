from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from turf.models import tbl_turf
from django.db import models

# Create your views here.


def turfowner(request):
    return render(request,"turfowner.htm")


def addturf(request):
    return render(request,"addturf.htm")


def turf_add(request):
    if request.method == 'POST':
        data = tbl_turf()
        data.turf_id = "na"
        data.turf_name = request.POST.get('Turfname')
        data.contact_no = request.POST.get('contactnumber')
        data.email = request.POST.get('email')
        data.working_hrs = request.POST.get('workinghrs')
        data.location = request.POST.get('location')
        data.fee = request.POST.get('fee')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name,Photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.status = "open"
        data.save()
        data.turf_id = "TF"+str(data.id)
        data.save()
    return render(request,"addturf.htm")

def view_turf(request):
    data=tbl_turf.objects.all()
    return render(request,"viewturf.htm", {'data1':data})



