from django.urls import path,include
from User import views
app_name='User'

urlpatterns = [
   
   path('HomePage/',views.HomePage, name="HomePage"),
   path('Userconcern/',views.Userconcern, name="Userconcern"),
   path('deleteuserconcern/<int:did>',views.deleteuserconcern, name="deleteuserconcern"),
   # path('edituserconcern/<int:eid>',views.edituserconcern, name="edituserconcern"),
   path('MyProfile/',views.MyProfile, name="MyProfile"),
   path('EditProfile/',views.EditProfile, name="EditProfile"),
   path('ProductSuggestion/',views.ProductSuggestion, name="ProductSuggestion"),
   #path('Viewphoto/<int:id>',views.Viewphoto, name="Viewphoto"),
   path('profile/',views.profile, name="profile"),
   path('ChangePassword/',views.ChangePassword, name="ChangePassword"),
   path('Complaint/',views.Complaint, name="Complaint"),
   path('ViewInfo/',views.ViewInfo, name="ViewInfo"),
   path('ViewNews/',views.ViewNews, name="ViewNews"),
   path('routine/',views.routine, name="routine"),
   path('tips/',views.tips, name="tips"),
   path('Ingredient/',views.Ingredient, name="Ingredient"),
   path('ajaxsearchproduct/',views.ajaxsearchproduct, name="ajaxsearchproduct"),
   path('Findskin/',views.Findskin, name="Findskin"),
   path('logout/',views.logout, name="logout"),


]