from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

# Create your views here.


def UserRegistration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        photo=request.FILES.get('photo')
        tbl_user.objects.create(user_name=name,
                                user_email=email,
                                user_contact=contact,
                                user_address=address,
                                user_age=age,
                                user_gender=gender,
                                user_password=password,
                                user_photo=photo)
        return render(request, 'Guest/UserRegistration.html',{'msg':'Registration Successfull'})
    else:
        return render(request, 'Guest/UserRegistration.html')
    

def Login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        if admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['adminid']=admindata.id
            return redirect('Admin:HomePage')

        elif usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['userid']=userdata.id
            return redirect('User:HomePage')
            
        else:
            return render(request, 'Guest/Login.html',{'msg':'Invalid Email or Password'})
    else:
        return render(request, 'Guest/Login.html')

def Index(request):
    return render(request, 'Guest/Index.html')

def Logout(request):
    if 'userid' in request.session:
        del request.session["userid"]
    if 'adminid' in request.session:
        del request.session["adminid"]
    return redirect("Guest:Login")


