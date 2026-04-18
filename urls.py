from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('login', views.login,name="login"),
    path('logout', views.logout,name="logout"),
    path('admin', views.admin,name="admin"),
    path('registerHospital', views.registerHospital,name="registerHospital"),
    path('adminHospitalList', views.adminHospitalList,name="adminHospitalList"),
    path('adminEditHospital', views.adminEditHospital,name="adminEditHospital"),
    path('adminRegisterDoctor', views.adminRegisterDoctor,name="adminRegisterDoctor"),
    path('adminDoctorList', views.adminDoctorList,name="adminDoctorList"),
    path('adminEditDoctor', views.adminEditDoctor,name="adminEditDoctor"),
    path('adminRegisterStaff', views.adminRegisterStaff,name="adminRegisterStaff"),
    path('adminStaffList', views.adminStaffList,name="adminStaffList"),
    path('adminEditStaff', views.adminEditStaff,name="adminEditStaff"),
    path('adminRegisterDepartment', views.adminRegisterDepartment,name="adminRegisterDepartment"),
    path('adminDepartmentList', views.adminDepartmentList,name="adminDepartmentList"),
    path('adminEditDepartment', views.adminEditDepartment,name="adminEditDepartment"),
    path('adminRegisterPolice', views.adminRegisterPolice,name="adminRegisterPolice"),
    path('adminPoliceList', views.adminPoliceList,name="adminPoliceList"),
    path('adminEditPolice', views.adminEditPolice,name="adminEditPolice"),
    path('adminRegisterAmbulance', views.adminRegisterAmbulance,name="adminRegisterAmbulance"),
    path('adminAmbulanceList', views.adminAmbulanceList,name="adminAmbulanceList"),
    path('adminEditAmbulance', views.adminEditAmbulance,name="adminEditAmbulance"),
    path('adminAccidentList', views.adminAccidentList,name="adminAccidentList"),
    path('adminViewComplaint', views.adminViewComplaint,name="adminViewComplaint"),


    
    path('user', views.user,name="user"),
    path('userRegister', views.userRegister,name="userRegister"),
    path('userSearchHospital', views.userSearchHospital,name="userSearchHospital"),
    path('userHospitalDetails', views.userHospitalDetails,name="userHospitalDetails"),
    path('userSearchAmbulance', views.userSearchAmbulance,name="userSearchAmbulance"),
    path('userSearchPolice', views.userSearchPolice,name="userSearchPolice"),
    path('userReportAccident', views.userReportAccident,name="userReportAccident"),
    path('userReportList', views.userReportList,name="userReportList"),
    path('userAddComplaint', views.userAddComplaint,name="userAddComplaint"),



    path('privacy', views.privacy,name="privacy"),
    path('Privacy', views.privacy,name="privacy"),
    path('profile', views.profile,name="profile"),
    path('Profile', views.profile,name="profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)