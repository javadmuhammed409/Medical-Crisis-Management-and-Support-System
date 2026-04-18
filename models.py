from datetime import date
from telnetlib import STATUS
from django.db import models

# Create your models here.

class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=100)
    password = models.CharField("password",max_length=100)
    role=models.CharField('role',max_length=10)

class location(models.Model):
    locid = models.AutoField(primary_key=True)
    location = models.CharField("location",max_length=100)

class department(models.Model):
    departid = models.AutoField(primary_key=True)
    departname = models.CharField("departname",max_length=100)
    departdesc = models.CharField("departdesc",max_length=100)

class user(models.Model):
    userid=models.AutoField(primary_key=True)
    name=models.CharField("username",max_length=100)
    phone=models.CharField("userphone",max_length=100)
    email=models.CharField("useremail",max_length=100)
    address=models.CharField("useraddress",max_length=300)
    pin=models.CharField("pin",max_length=300)
    date = models.CharField("date",max_length=30)
    status = models.CharField("status",max_length=30)
    emergency = models.CharField("emergency",max_length=100)
    login = models.ForeignKey(login,on_delete=models.CASCADE,null=True)

class hospital(models.Model):
    hospid = models.AutoField(primary_key=True)
    hospname = models.CharField("hospname",max_length=100)
    hospdesc = models.CharField("hospdesc",max_length=300)
    facilities = models.CharField("facilities",max_length=300)
    location = models.ForeignKey(location,on_delete=models.CASCADE,null=True)
    @property
    def getStaffs(self):
        return staff.objects.filter(hospital=self)
    
    @property
    def getDoctors(self):
        return doctor.objects.filter(hospital=self)

class doctor(models.Model):
    docid = models.AutoField(primary_key=True)
    docname = models.CharField("docname",max_length=100)
    docdesc = models.CharField("docdesc",max_length=300)
    hospital = models.ForeignKey(hospital,on_delete=models.CASCADE,null=True)
    department = models.ForeignKey(department,on_delete=models.CASCADE,null=True)

class staff(models.Model):
    staffid = models.AutoField(primary_key=True)
    staffname = models.CharField("staffname",max_length=100)
    staffaddress = models.CharField("staffaddress",max_length=100)
    staffphone = models.CharField("staffphone",max_length=100)
    staffdesc = models.CharField("staffdesc",max_length=100)
    staffdepart = models.ForeignKey(department,on_delete=models.CASCADE,null=True)
    hospital = models.ForeignKey(hospital,on_delete=models.CASCADE,null=True)

class ambulance(models.Model):
    ambid = models.AutoField(primary_key=True)
    ambname = models.CharField("ambname",max_length=100)
    ambphone = models.CharField("ambaddress",max_length=100)
    amblocation = models.ForeignKey(location,on_delete=models.CASCADE,null=True)

class police(models.Model):
    policeid = models.AutoField(primary_key=True)
    name=models.CharField("name",max_length=100)
    phone=models.CharField("phone",max_length=100)
    email=models.CharField("email",max_length=100)
    address=models.CharField("address",max_length=300)
    location = models.ForeignKey(location,on_delete=models.CASCADE,null=True)

class complaint(models.Model):
    compid = models.AutoField(primary_key=True)
    user = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    complaint = models.CharField("complaint",max_length=300)

class accident(models.Model):
    accid = models.AutoField(primary_key=True)
    accidenttype = models.CharField("accidenttype",max_length=100)
    accident = models.CharField("accident",max_length=300)
    description = models.CharField("description",max_length=300)
    location = models.ForeignKey(location,on_delete=models.CASCADE,null=True)
    date = models.CharField("date",max_length=50)
    time = models.CharField("time",max_length=50)
    user = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    police = models.ForeignKey(police,on_delete=models.CASCADE,null=True)
