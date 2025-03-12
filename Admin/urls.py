from django.urls import path,include
from Admin import views
app_name='Admin'
urlpatterns = [
    path('HomePage/',views.HomePage, name="HomePage"),
    path('Admin/',views.Admin, name="Admin"),

    path('AgeLimit/',views.Agelimit, name="Agelimit"),
    path('deleteagelimit/<int:did>',views.deleteagelimit, name="deleteagelimit"),
    path('editagelimit/<int:eid>',views.editagelimit, name="editagelimit"),

    path('Category/',views.Category, name="Category"),
    path('deletecategory/<int:did>',views.deletecategory, name="deletecategory"),
    path('editcategory/<int:eid>',views.editcategory, name="editcategory"),

    path('Concern/',views.Concern, name="Concern"),
    path('deleteconcern/<int:did>',views.deleteconcern, name="deleteconcern"),
    path('editconcern/<int:eid>',views.editconcern, name="editconcern"),


    path('District/',views.District, name="District"),
    path('deletedistrict/<int:did>',views.deletedistrict, name="deletedistrict"),
    path('editdistrict/<int:eid>',views.editdistrict, name="editdistrict"),


    path('Gender/',views.Gender, name="Gender"),
    path('deletegender/<int:did>',views.deletegender, name="deletegender"),
    path('editgender/<int:eid>',views.editgender, name="editgender"),
    path('Info/',views.Info, name="Info"),
    path('deleteinfo/<int:did>',views.deleteinfo, name="deleteinfo"),
    path('editinfo/<int:eid>',views.editinfo, name="editinfo"),

    path('Product/',views.Product, name="Product"),
    path('deleteproduct/<int:did>',views.deleteproduct, name="deleteproduct"),
    path('editproduct/<int:eid>',views.editproduct, name="editproduct"),
    path('SkinProduct/<int:id>',views.SkinProduct, name="SkinProduct"),
    path('deleteskinproduct/<int:did>/<int:pid>',views.deleteskinproduct, name="deleteskinproduct"),
    path('editskinproduct/<int:eid>/<int:pid>',views.editskinproduct, name="editskinproduct"),
    path('Gallery/<int:id>',views.gallery, name="gallery"),
    path('delproductphoto/<int:did>',views.delproductphoto, name="delproductphoto"),

   
    path('ViewComplaint/',views.ViewComplaint, name="ViewComplaint"),
    path('Reply/<int:id>',views.Reply, name="Reply"),

    path('Skintype/',views.Skintype, name="Skintype"),
    path('deleteskintype/<int:did>',views.deleteskintype, name="deleteskintype"),
    path('editskintype/<int:eid>',views.editskintype, name="editskintype"),
    path('News/',views.News, name="News"),
    path('deletenews/<int:did>',views.deletenews, name="deletenews"),
    path('ProductSkintype/<int:id>',views.ProductSkintype, name="ProductSkintype"),
    path('deleteproductskintype/<int:did>/<int:pid>',views.deleteproductskintype, name="deleteproductskintype"),
    path('editproductskintype/<int:eid>/<int:pid>',views.editproductskintype, name="editproductskintype"),

    path('logout/', views.logout, name="logout"),

]