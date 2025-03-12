from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *

def logout(request):
    del request.session['adminid']
    return redirect("Guest:Login")

def HomePage(request):
    if "adminid" in request.session:
        return render(request,"Admin/HomePage.html")
    else:
        return redirect("Guest:Login")

def Admin(request):
    # if "adminid" in request.session:
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,"Admin/Admin.html")
    else:
        return render(request,"Admin/Admin.html")
    # else:
    #     return redirect("Guest:Login")

def Agelimit(request):
    if "adminid" in request.session:
        agedata=tbl_agelimit.objects.all()
        print(agedata)
        if request.method=='POST':
            agelimit=request.POST.get('limit')
            tbl_agelimit.objects.create(age_limit=agelimit)
            return redirect('Admin:Agelimit')
        else:
            return render(request,"Admin/Agelimit.html",{'age':agedata})
    else:
        return redirect("Guest:Login")
        
def editagelimit(request,eid):
    editdata=tbl_agelimit.objects.get(id=eid)
    if request.method =="POST":
        editdata.age_limit=request.POST.get('limit')
        editdata.save()
        return redirect('Admin:Agelimit')
    else:
        return render(request,"Admin/Agelimit.html",{'type':editdata})

    
def deleteagelimit(request,did):
    tbl_agelimit.objects.get(id=did).delete()
    return redirect('Admin:Agelimit')


def Category(request):
    if "adminid" in request.session:
        catdata=tbl_category.objects.all()
        print(catdata)
        if request.method=='POST':
            categoryname=request.POST.get('name')
            tbl_category.objects.create(category_name=categoryname)
            return redirect('Admin:Category')
        else:
            return render(request,"Admin/Category.html",{'cat':catdata})
    else:
        return redirect("Guest:Login")
    
def deletecategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect('Admin:Category')

def editcategory(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method =="POST":
        editdata.category_name=request.POST.get('name')
        editdata.save()
        return redirect('Admin:Category')
    else:
        return render(request,"Admin/Category.html",{'type':editdata})
    

def Concern(request):
    if "adminid" in request.session:
        condata=tbl_concern.objects.all()
        print(condata)
        if request.method=='POST':
            concerns=request.POST.get('concern')
            photo=request.FILES.get('selconvern')
            details=request.POST.get('txt_details')
            tbl_concern.objects.create(concern_name=concerns,concern_photo=photo,concern_details=details)
            return redirect('Admin:Concern')
        else:
            return render(request,"Admin/Concern.html",{'con':condata})
    else:
        return redirect("Guest:Login")

def deleteconcern(request,did):
    tbl_concern.objects.get(id=did).delete()
    return redirect('Admin:Concern')

def editconcern(request,eid):
    editdata=tbl_concern.objects.get(id=eid)
    if request.method =="POST":
        editdata.concern_name=request.POST.get('concern')
        editdata.save()
        return redirect('Admin:Concern')
    else:
        return render(request,"Admin/Concern.html",{'type':editdata})

def District(request):
    if "adminid" in request.session:
        disdata=tbl_district.objects.all()
        print(disdata)
        if request.method=='POST':
            districtname=request.POST.get('name')
            tbl_district.objects.create(district_name=districtname)
            return redirect('Admin:District')
        else:
            return render(request,"Admin/District.html",{'dis':disdata})
    else:
        return redirect("Guest:Login")

def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')

def editdistrict(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method =="POST":
        editdata.district_name=request.POST.get('name')
        editdata.save()
        return redirect('Admin:District')
    else:
        return render(request,"Admin/District.html",{'type':editdata})


def Gender(request):
    if "adminid" in request.session:
        gendata=tbl_gender.objects.all()
        print(gendata)
        if request.method=='POST':
            gendername=request.POST.get('gender')
            tbl_gender.objects.create(gender=gendername)
            return redirect('Admin:Gender')
        else:
            return render(request,"Admin/Gender.html",{'gen':gendata})
    else:
        return redirect("Guest:Login")

def deletegender(request,did):
    tbl_gender.objects.get(id=did).delete()
    return redirect('Admin:Gender')

def editgender(request,eid):
    editdata=tbl_gender.objects.get(id=eid)
    if request.method =="POST":
        editdata.gender=request.POST.get('gender')
        editdata.save()
        return redirect('Admin:Gender')
    else:
        return render(request,"Admin/Gender.html",{'type':editdata})

def Product(request):
    if "adminid" in request.session:
        concerns=tbl_concern.objects.all()
        productdata=tbl_product.objects.all()
        if request.method=='POST':
            name=request.POST.get('name')
            details=request.POST.get('details')
            price=request.POST.get('price')
            amlink=request.POST.get('amazonLink')
            fclink=request.POST.get('flipkartLink')
            concern=request.POST.get('sel_concern')
            tbl_product.objects.create(product_name=name,
                                    product_price=price,
                                    product_details=details,
                                    product_amzonlink=amlink,
                                    product_flpctlink=fclink,
                                    concern=tbl_concern.objects.get(id=concern))
            return redirect('Admin:Product')
        else:
            return render(request,"Admin/Product.html",{'pro':productdata,'concern':concerns})
    else:
        return redirect("Guest:Login")

def deleteproduct(request,did):
    tbl_product.objects.get(id=did).delete()
    return redirect('Admin:Product')

def editproduct(request,eid):
    editdata=tbl_product.objects.get(id=eid)
    if request.method =="POST":
        editdata.product_name=request.POST.get('name')
        editdata.product_details=request.POST.get('details')
        editdata.product_price=request.POST.get('price')
        editdata.product_amzonlink=request.POST.get('amazonLink')
        editdata.product_flpctlink=request.POST.get('flipkartLink')
        editdata.save()
        return redirect('Admin:Product')
    else:
        return render(request,"Admin/Product.html",{'type':editdata})

def gallery(request,id):
    imgdata=tbl_gallery.objects.filter(product=id)
    if request.method=='POST':
        img=request.FILES.get('photo')
        productid=tbl_product.objects.get(id=id)
        tbl_gallery.objects.create(gallery_image=img,product=productid)
        return redirect('Admin:gallery',id)
    else:
        return render(request,"Admin/Gallery.html",{'img':imgdata})

def delproductphoto(request,did):
    id=tbl_gallery.objects.get(id=did).product.id
    tbl_gallery.objects.get(id=did).delete()
    return redirect('Admin:gallery',id)

def SkinProduct(request,id):
    if "adminid" in request.session:
        skinproduct=tbl_skintype.objects.all()
        sknprodata=tbl_skinproduct.objects.filter(product=id)
        if request.method=='POST':
            skinname=request.POST.get('skinType')
            tbl_skinproduct.objects.create(skinproduct_type=tbl_skintype.objects.get(id=skinname),product=tbl_product.objects.get(id=id))
            return redirect('Admin:SkinProduct',id)
        else:
            return render(request,"Admin/SkinProduct.html",{'sknpro':sknprodata,'skintype':skinproduct,'pid':id})
    else:
        return redirect("Guest:Login")
    
def deleteskinproduct(request,did,pid):
    tbl_skinproduct.objects.get(id=did).delete()
    return redirect('Admin:SkinProduct',pid)

def editskinproduct(request,eid,pid):
    skintype=tbl_skintype.objects.all()
    editdata=tbl_skinproduct.objects.get(id=eid)
    if request.method =="POST":
        editdata.skinproduct_type=tbl_skintype.objects.get(id=request.POST.get("skin_type"))
        editdata.save()
        return redirect('Admin:SkinProduct',pid)
    else:
        return render(request,"Admin/SkinProduct.html",{'edit':editdata,'skintype':skintype,'pid':pid})

def Info(request):
    if "adminid" in request.session:
        return render(request,"Admin/Info.html")
    else:
        return redirect("Guest:Login")

def Skintype(request):
    if "adminid" in request.session:
        skndata=tbl_skintype.objects.all()
        print(skndata)
        if request.method=='POST':
            skintype=request.POST.get('skintype')
            tbl_skintype.objects.create(skin_type=skintype)
            return redirect('Admin:Skintype')
        else:
            return render(request,"Admin/Skintype.html",{'skn':skndata})
    else:
        return redirect("Guest:Login")

def deleteskintype(request,did):
    tbl_skintype.objects.get(id=did).delete()
    return redirect('Admin:Skintype')

def editskintype(request,eid):
    editdata=tbl_skintype.objects.get(id=eid)
    if request.method == "POST":
        editdata.skin_type=request.POST.get('skintype')
        editdata.save()
        return redirect('Admin:Skintype')
    else:
         return render(request,"Admin/Skintype.html",{'type':editdata})

def News(request):
    if "adminid" in request.session:
        newsdata=tbl_news.objects.all()
        print(newsdata)
        if request.method=='POST':
            newscontent=request.POST.get('content')
            newsphoto=request.FILES.get('photo')
            tbl_news.objects.create(news_content=newscontent,news_photo=newsphoto)
            return redirect('Admin:News')
        else:
            return render(request,"Admin/News.html",{'new':newsdata})
    else:
        return redirect("Guest:Login")

def deletenews(request,did):
    tbl_news.objects.get(id=did).delete()
    return redirect('Admin:News')

def ProductSkintype(request,id):
    if "adminid" in request.session:
        
        skintype=tbl_skintype.objects.all()
        proskndata=tbl_productskintype.objects.filter(product=id)
        print(proskndata)
        if request.method=='POST':
            skinname=request.POST.get('skin_type')
            tbl_productskintype.objects.create(product_skintype=tbl_skintype.objects.get(id=skinname),product=tbl_product.objects.get(id=id))
            return redirect('Admin:ProductSkintype',id)
        else:
            return render(request,"Admin/ProductSkintype.html",{'proskn':proskndata,'skintype':skintype,'pid':id})
    else:
        return redirect("Guest:Login")

def deleteproductskintype(request,did,pid):
    tbl_productskintype.objects.get(id=did).delete()
    return redirect('Admin:ProductSkintype',pid)

def editproductskintype(request,eid,pid):
    skintype=tbl_skintype.objects.all()
    editdata=tbl_productskintype.objects.get(id=eid)
    if request.method =="POST":
        editdata.product_skintype=tbl_skintype.objects.get(id=request.POST.get("skin_type"))
        editdata.save()
        return redirect('Admin:ProductSkintype',pid)
    else:
        return render(request,"Admin/ProductSkintype.html",{'edit':editdata,'skintype':skintype,'pid':pid})

def Info(request):
    if "adminid" in request.session:
        infodata=tbl_info.objects.all()
        print(infodata)
        if request.method=='POST':
            inquestion=request.POST.get('question')
            inanswer=request.POST.get('answer')
            tbl_info.objects.create(question=inquestion,answer=inanswer)
            return redirect('Admin:Info')
        else:
            return render(request,"Admin/Info.html",{'inf':infodata})
    else:
        return redirect("Guest:Login")

def deleteinfo(request,did):
    tbl_info.objects.get(id=did).delete()
    return redirect('Admin:Info')

def editinfo(request,eid):
    editdata=tbl_info.objects.get(id=eid)
    if request.method =="POST":
        editdata.question=request.POST.get('question')
        editdata.answer=request.POST.get('answer')
        editdata.save()
        return redirect('Admin:Info')
    else:
        return render(request,"Admin/Info.html",{'type':editdata})
    
def ViewComplaint(request):
    if "adminid" in request.session:
        complaintdata=tbl_complaint.objects.all()
        return render(request,"Admin/ViewComplaint.html",{'comp':complaintdata})
    else:
        return redirect("Guest:Login")
    
def Reply(request,id):
    replydata=tbl_complaint.objects.get(id=id)
    if request.method=='POST':
        reply=request.POST.get('content')
        replydata.reply=reply
        replydata.save()
        return redirect('Admin:ViewComplaint')
    else:
        return render(request,'Admin/Reply.html',{'reply':replydata})
