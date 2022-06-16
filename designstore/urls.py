from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.designstore, name="designstore"),
    path('cart/', views.cart, name="cart"),
    path('viewitem/', views.viewitem, name="viewitem"),
    #path('form_page/', views.cart, name="formpage"),
    path('formpage/', views.form_name_view, name="form_name"),
    path('viewlogo/', views.viewlogo, name="viewlogo"),
	path('viewicon/', views.viewicon, name="viewicon"),
    #path('login/', views.form_name_view, name="form_name"),
    #path('login/', views.sitelogin, name="login"),
    path('sign_up/', views.sign_up, name='sign_up'),
	
]