import email
from django.shortcuts import render
from django.shortcuts import render,redirect
import datetime
import time
from datetime import date
from datetime import datetime
from django.db.models import Q
from .models import login as log, user as usr,hospital as hos, doctor as doc, staff as stf, ambulance as amb, police as pol, complaint as com , accident as acc, location as loc , department as dep

# Create your views here.

def index(request):
    # dist = dst.objects.all()
    try:
        msg = request.GET['msg']
    except:
        msg = ""
    return render(request,"index.html",{"msg":msg})

def login(request):
    if request.POST:
        user = request.POST["username"]
        pswd = request.POST["password"]
        
        datac = log.objects.filter(username=user, password=pswd).count()
        if datac==1:
            data = log.objects.get(username = user, password = pswd)
            if (data.role == "admin"):
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.logid
                response = redirect('/admin')
                return response
            elif (data.role == "user"):
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.logid
                response = redirect('/user')
                return response
        else:
            response = redirect('/index?msg=Invalid username or password')
            return response
    else:
        response = redirect('/index')
        return response

def logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index?id=logout")
        return response
    except:
        response = redirect("/index?id=logout")
        return response

def admin(request):
    if(request.session.get('role', ' ') == "admin"):
        return render(request,"admin.html")
    else:
        response = redirect('/index'+"?msg=Session expired , login again")
        return response

def registerHospital(request):
    msg = ""
    if request.POST:
        name = request.POST['name']
        desc = request.POST['desc']
        loca = loc.objects.get(locid = request.POST['loca'])
        facilities = request.POST['facilities']

        hos.objects.create(hospname = name, hospdesc = desc, facilities = facilities, location = loca)
        msg = "Registered"
    location = loc.objects.all().order_by('location')
    return render(request,"adminRegisterHospital.html",{"msg":msg, "location":location})

def adminHospitalList(request):
    if request.POST:
        id = request.POST['id']
        hos.objects.filter(hospid = id).delete()
    data = hos.objects.all()
    location = loc.objects.all().order_by('location')
    return render(request,"adminHospitalList.html",{"data":data, "location":location})

def adminEditHospital(request):
    if request.POST:
        id = request.POST['id']
        name = request.POST['name']
        desc = request.POST['desc']
        loca = loc.objects.get(locid = request.POST['loca'])
        facilities = request.POST['facilities']
        hos.objects.filter(hospid = id).update(hospname = name, hospdesc = desc, facilities = facilities, location = loca)
    
    response = redirect('/adminHospitalList')
    return response

def adminRegisterDoctor(request):
    msg = ""
    if request.POST:
        name = request.POST['name']
        desc = request.POST['desc']
        dept = dep.objects.get(departid = request.POST['dept'])
        hosp = hos.objects.get(hospid=request.POST['hosp'])
        doc.objects.create(docname = name, docdesc = desc, hospital = hosp, department = dept)
        msg = "Registered"

    hospital = hos.objects.all()
    department = dep.objects.all()
    return render(request,"adminRegisterDoctor.html",{"msg":msg, "hospital":hospital, "department":department})
    
def adminDoctorList(request):
    if request.POST:
        id = request.POST['id']
        doc.objects.filter(docid = id).delete()

    data = doc.objects.all()
    hospital = hos.objects.all()
    department = dep.objects.all()
    return render(request,"adminDoctorList.html",{"data":data, "hospital":hospital, "department":department})

def adminEditDoctor(request):
    if request.POST:
        id = request.POST['id']
        name = request.POST['name']
        desc = request.POST['desc']
        dept = dep.objects.get(departid = request.POST['dept'])
        hosp = hos.objects.get(hospid=request.POST['hosp'])

        doc.objects.filter(docid = id).update(docname = name, docdesc = desc, hospital = hosp, department = dept)
    
    response = redirect('/adminDoctorList')
    return response

def adminRegisterStaff(request):
    msg = ""
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        desc = request.POST['desc']
        address = request.POST['address']
        dept = dep.objects.get(departid = request.POST['dept'])
        hosp = hos.objects.get(hospid=request.POST['hosp'])

        stf.objects.create(staffname = name, staffphone = phone, staffdesc = desc, staffaddress = address, hospital = hosp, staffdepart = dept)
        msg = "Registered"

    hospital = hos.objects.all()
    department = dep.objects.all()
    return render(request,"adminRegisterStaff.html",{"msg":msg, "hospital":hospital, "department": department})
    
def adminStaffList(request):
    if request.POST:
        id = request.POST['id']
        stf.objects.filter(staffid = id).delete()

    data = stf.objects.all()
    hospital = hos.objects.all()
    department = dep.objects.all()
    return render(request,"adminStaffList.html",{"data":data, "hospital":hospital, "department": department})

def adminEditStaff(request):
    if request.POST:
        id = request.POST['id']
        name = request.POST['name']
        phone = request.POST['phone']
        desc = request.POST['desc']
        address = request.POST['address']
        dept = dep.objects.get(departid = request.POST['dept'])
        hosp = hos.objects.get(hospid=request.POST['hosp'])

        stf.objects.filter(staffid = id).update(staffname = name, staffphone = phone, staffdesc = desc, staffaddress = address, hospital = hosp, staffdepart = dept)
    
    response = redirect('/adminStaffList')
    return response

def adminRegisterDepartment(request):
    msg = ""
    if request.POST:
        name = request.POST['name']
        desc = request.POST['desc']

        dep.objects.create(departname = name, departdesc = desc)
        msg = "Registered"

    return render(request,"adminRegisterDepartment.html",{"msg":msg})
    
def adminDepartmentList(request):
    if request.POST:
        id = request.POST['id']
        dep.objects.filter(departid = id).delete()

    data = dep.objects.all()
    return render(request,"adminDepartmentList.html",{"data":data})

def adminEditDepartment(request):
    if request.POST:
        id = request.POST['id']
        dept = request.POST['dept']
        desc = request.POST['desc']
        dep.objects.filter(departid = id).update(departname = dept, departdesc = desc)
    
    response = redirect('/adminDepartmentList')
    return response

def adminRegisterPolice(request):
    msg = ""
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        loca = loc.objects.get(locid = request.POST['loca'])

        pol.objects.create(name = name, phone = phone, email = email, address = address, location = loca)
        msg = "Registered"
        
    location = loc.objects.all()
    return render(request,"adminRegisterPolice.html",{"msg":msg, "location":location})
    
def adminPoliceList(request):
    if request.POST:
        id = request.POST['id']
        pol.objects.filter(policeid = id).delete()

    data = pol.objects.all()
    location = loc.objects.all()
    return render(request,"adminPoliceList.html",{"data":data, "location":location})

def adminEditPolice(request):
    if request.POST:
        id = request.POST['id']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        loca = loc.objects.get(locid = request.POST['loca'])
        pol.objects.filter(policeid = id).update(name = name, phone = phone, email = email, address = address, location = loca)
    
    response = redirect('/adminPoliceList')
    return response

def adminRegisterAmbulance(request):
    msg = ""
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        loca = loc.objects.get(locid = request.POST['loca'])

        amb.objects.create(ambname = name, ambphone = phone, amblocation = loca)
        msg = "Registered"

    location = loc.objects.all()
    return render(request,"adminRegisterAmbulance.html",{"msg":msg,"location":location})

def adminAmbulanceList(request):
    if request.POST:
        id = request.POST['id']
        amb.objects.filter(ambid = id).delete()

    data = amb.objects.all()
    location = loc.objects.all()
    return render(request,"adminAmbulanceList.html",{"data":data, "location":location})

def adminEditAmbulance(request):
    if request.POST:
        id = request.POST['id']
        name = request.POST['name']
        phone = request.POST['phone']
        loca = loc.objects.get(locid = request.POST['loca'])
        amb.objects.filter(ambid = id).update(ambname = name, ambphone = phone, amblocation = loca)
    
    response = redirect('/adminAmbulanceList')
    return response

def adminAccidentList(request):
    if request.POST:
        id = request.POST['id']
        police = pol.objects.get(policeid = request.POST['police'])
        acc.objects.filter(accid = id).update(police = police)

    data = acc.objects.all()
    police = pol.objects.all()
    return render(request,"adminAccidentList.html",{"data":data, "police":police})

def adminViewComplaint(request):
    msg = ""
    data = com.objects.all()
    return render(request,"adminViewComplaint.html",{"msg":msg,"data":data})




def userRegister(request):
    msg = ""
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        pin = request.POST['pin']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['password']
        today = date.today()

        log.objects.create(username = username, password = password, role = "user")
        tt = log.objects.last()

        usr.objects.create(name = name, phone = phone, email = email, address = address, date = today, pin = pin, status = '1', login = tt)
        msg = "Registered"

    return render(request,"userRegister.html",{"msg":msg})

def user(request):
    if(request.session.get('role', ' ') == "user"):
        user = usr.objects.get(login = request.session['id'])
        return render(request,"user.html",{"user":user})
    else:
        response = redirect('/index'+"?msg=Session expired , login again")
        return response

def userSearchHospital(request):
    msg = ""
    data = ""
    if request.POST:
        search = request.POST['search']
        data = hos.objects.filter(location__location__icontains = search)   #icontains means case insensitive contains


    user = usr.objects.get(login = request.session['id'])
    return render(request,"userSearchHospital.html",{"data":data, "user":user, "msg":msg})

def userHospitalDetails(request):
    msg = ""
    id = request.GET['id']
    user = usr.objects.get(login = request.session['id'])
    data = hos.objects.get(hospid = id)
    return render(request,"userHospitalDetails.html",{"msg":msg, "user":user, "data":data})
    
def userSearchAmbulance(request):
    msg = ""
    data = ""
    if request.POST:
        search = request.POST['search']
        data = amb.objects.filter(amblocation__location__icontains = search)   #icontains means case insensitive contains

    user = usr.objects.get(login = request.session['id'])
    return render(request,"userSearchAmbulance.html",{"data":data, "user":user, "msg":msg})
    
def userSearchPolice(request):
    msg = ""
    data = ""
    if request.POST:
        search = request.POST['search']
        data = pol.objects.filter(location__location__icontains = search)   #icontains means case insensitive contains

    user = usr.objects.get(login = request.session['id'])
    return render(request,"userSearchPolice.html",{"data":data, "user":user, "msg":msg})
    
def userReportAccident(request):
    msg = ""
    if request.POST:
        acctype = request.POST['acctype']
        accident = request.POST['accident']
        desc = request.POST['desc']
        loca = loc.objects.get(locid = request.POST['loca'])
        dates = request.POST['date']
        current_time = request.POST['time']
        userid = usr.objects.get(login = request.session['id'])

        acc.objects.create(accidenttype = acctype, accident = accident, description = desc, location = loca, date = dates, time = current_time, user = userid)
        msg = "Registered"

    user = usr.objects.get(login = request.session['id'])
    today = date.today().strftime('%Y-%m-%d')
    location = loc.objects.order_by('location').all() 
    return render(request,"userReportAccident.html",{"location":location, "user":user, "msg":msg, "today":today})

def userReportList(request):
    userid = usr.objects.get(login = request.session['id'])
    data = acc.objects.filter(user = userid.userid).all()
    return render(request,"userReportList.html",{"data":data})
    
def userAddComplaint(request):
    msg = ""
    user = usr.objects.get(login = request.session['id'])
    if request.POST:
        if request.POST['action'] == 'add':
            comp = request.POST['comp']
            com.objects.create(complaint = comp, user = user)
            msg = "Registered"
        
        elif request.POST['action'] == 'delete':
            id = request.POST['id']
            com.objects.filter(compid = id).delete()

    data = com.objects.filter(user = user.userid).all()
    return render(request,"userAddComplaint.html",{"msg":msg,"data":data,"user":user})

def privacy(request):
    msg=""
    user = ""
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        id=request.session["id"]
        data=log.objects.get(logid=id)
        if data.password==t1:
            msg="sucessfully updated"
            log.objects.filter(logid=id).update(password=t2)
        else:
            msg="invalid current password"

    returnpage="admin.html"
    if(request.session['role']=="admin"):
        returnpage="admin.html"
    elif request.session["role"] =="user":
        returnpage="user.html"
        user = usr.objects.get(login = request.session['id'])
    return render(request, "privacy.html",{"role":returnpage,"msg":msg, "user":user})
    
def profile(request):
    msg=""
    user = usr.objects.get(login = request.session['id'])
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        t3=request.POST["t3"]
        t4=request.POST["t4"]
        t5=request.POST["t5"]
        
        usr.objects.filter(userid = user.userid).update(name = t1 , phone = t2 , email = t3 , address = t4, pin = t5)
        msg="Profile updated"

    user = usr.objects.get(login = request.session['id'])
    return render(request, "profile.html",{"user":user,"msg":msg})