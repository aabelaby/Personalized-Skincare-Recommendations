from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from User.models import *

# Create your views here.

def logout(request):
    del request.session['userid']
    return redirect("Guest:Login")

def HomePage(request):
    if "userid" in request.session:
        return render(request, 'User/HomePage.html')
    else:
        return redirect("Guest:Login")

def Userconcern(request):
    userconcerndata=tbl_userconcern.objects.all()
    if "userid" in request.session:
        sknconcern=tbl_concern.objects.all()
        userid=tbl_user.objects.get(id=request.session['userid'])
        print(sknconcern)
        if request.method=='POST':
            usrcncrn=request.POST.get('skin_type')
            tbl_userconcern.objects.create(concern=tbl_concern.objects.get(id=request.POST.get('concern')),user=userid)
            return redirect('User:Userconcern')
        else:
            return render(request,"User/Userconcern.html",{'skinconcern':sknconcern,'pid':id,'data':userconcerndata})
    else:
        return redirect("Guest:Login")
    
def deleteuserconcern(request,did):
    tbl_userconcern.objects.get(id=did).delete()
    return redirect('User:Userconcern')

# def edituserconcern(request,eid):
#     userconcerndata=tbl_userconcern.objects.all()
#     sknconcern=tbl_concern.objects.all()
#     editdata=tbl_userconcern.objects.get(id=eid)
#     if request.method =="POST":
#         editdata.concern=tbl_concern.objects.get(id=request.POST.get('concern'))
#         editdata.save()
#         return redirect('User:Userconcern')
#     else:
#         return render(request,"User/Userconcern.html",{'type':editdata,'skinconcerns':sknconcern,'data':userconcerndata})

def Complaint(request):
    if "userid" in request.session:
        return render(request, 'User/Complaint.html')
    else:
        return redirect("Guest:Login")

def MyProfile(request):
    if "userid" in request.session:
        userdata=tbl_user.objects.get(id=request.session['userid'])
        return render(request, 'User/MyProfile.html',{'data':userdata})
    else:
        return redirect("Guest:Login")

def EditProfile(request):
    if "userid" in request.session:
        userdata=tbl_user.objects.get(id=request.session['userid'])
        if request.method=='POST':
            userdata.user_name=request.POST.get('name')
            userdata.user_email=request.POST.get('email')
            userdata.user_contact=request.POST.get('contact')
            userdata.user_address=request.POST.get('address')
            userdata.save()
            return render(request, 'User/EditProfile.html',{'msg':'Profile Updated','data':userdata})
        else:
            return render(request, 'User/EditProfile.html',{'data':userdata})
    else:
        return redirect("Guest:Login")

def profile(request):
    if "userid" in request.session:
        userdata=tbl_user.objects.get(id=request.session['userid'])
        if request.method=='POST':
            userdata.user_photo=request.FILES.get('photo')
            userdata.save()
            return render(request, 'User/ChoosePhoto.html',{'msg':'Profile Updated','data':userdata})
        else:
            return render(request, 'User/ChoosePhoto.html',{'data':userdata})
    else:
        return redirect("Guest:Login")
    
def ChangePassword(request):
    if "userid" in request.session:
        userdata=tbl_user.objects.get(id=request.session['userid'])
        if request.method=='POST':
            dbpassword=userdata.user_password
            currentpassword=request.POST.get('txt_current')
            newpassword=request.POST.get('txt_new')
            confirmpassword=request.POST.get('txt_confirm')
            if currentpassword==dbpassword:
                if newpassword==confirmpassword:
                    userdata.user_password=newpassword
                    userdata.save()
                    return render(request, 'User/ChangePassword.html',{'msg1':'Password Changed'})
                else:
                    return render(request, 'User/ChangePassword.html',{'msg':'New Password and Confirm Password not matched'})
            else:
                return render(request, 'User/ChangePassword.html',{'msg':'Current Password not matched'})
        else:   
            return render(request, 'User/ChangePassword.html')
    else:
        return redirect("Guest:Login")

def ProductSuggestion(request):
    userconcern=tbl_concern.objects.all()
    skintype=tbl_skintype.objects.all()
    if "userid" in request.session:
        suggdata=tbl_product.objects.all()
        image=tbl_gallery.objects.filter(product__in=suggdata)
        return render(request,"User/ProductSuggestion.html",{'inf':suggdata,'img':image, 'skinconcern':userconcern, 'skintype':skintype})
    else:
        return redirect("Guest:Login")
    
# def Viewphoto(request,id):
#     if "userid" in request.session:
#         image=tbl_gallery.objects.filter(product=id)
#         return render(request,"User/Viewphoto.html",{'img':image})
#     else:
#         return redirect("Guest:Login")
    
def ViewInfo(request):
    if "userid" in request.session:
        infodata=tbl_info.objects.all()
        return render(request,"User/ViewInfo.html",{'inf':infodata})
    else:
        return redirect("Guest:Login")

def ViewNews(request):
    if "userid" in request.session:
        newsdata=tbl_news.objects.all()
        return render(request,"User/ViewNews.html",{'new':newsdata})
    else:
        return redirect("Guest:Login")
    
def ajaxsearchproduct(request):
    if request.GET.get("skinid") != "" and request.GET.get("concernid") != "":
        skinpdt = tbl_product.objects.filter(tbl_productskintype__product_skintype=request.GET.get("skinid"))
        con = tbl_concern.objects.get(id=request.GET.get("concernid"))
        if con.concern_name == "No Concern":
            concernpdt = []
        else:
            concernpdt = tbl_product.objects.filter(concern=request.GET.get("concernid"))
        return render(request,"User/AjaxSearchProduct.html",{'skindata':skinpdt,"concerndata":concernpdt})
    elif request.GET.get("skinid") != "":
        skinpdt = tbl_product.objects.filter(tbl_productskintype__product_skintype=request.GET.get("skinid"))
        return render(request,"User/AjaxSearchProduct.html",{'skindata':skinpdt})
    elif request.GET.get("concernid") != "":
        con = tbl_concern.objects.get(id=request.GET.get("concernid"))
        if con.concern_name == "No Concern":
            concernpdt = []
        else:
            concernpdt = tbl_product.objects.filter(concern=request.GET.get("concernid"))
        return render(request,"User/AjaxSearchProduct.html",{'concerndata':concernpdt})
    else:
        pdt = tbl_product.objects.all()
        return render(request,"User/AjaxSearchProduct.html",{'data':pdt})
    
def Complaint(request):
    if "userid" in request.session:
        userid=tbl_user.objects.get(id=request.session['userid'])
        complaintdata=tbl_complaint.objects.all()
        if request.method=='POST':
            comptitle=request.POST.get('title')
            compcontent=request.POST.get('content')
            tbl_complaint.objects.create(title=comptitle,content=compcontent,user=userid)
            return redirect('User:Complaint')
        else:
            return render(request,"User/Complaint.html",{'comp':complaintdata})
    else:
        return redirect("Guest:Login")
    
def routine(request):
    if "userid" in request.session:
        return render(request, 'User/routine.html')
    else:
        return redirect("Guest:Login")

def tips(request):
    if "userid" in request.session:
        return render(request, 'User/tips.html')
    else:
        return redirect("Guest:Login")
    
def Ingredient(request):
    if "userid" in request.session:
        return render(request, 'User/Ingredient.html')
    else:
        return redirect("Guest:Login")