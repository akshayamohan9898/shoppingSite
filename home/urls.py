from django.urls import path
from . import views

urlpatterns = [
    path('call/',views.call),
    path('home/',views.home),
    path('add',views.add),
    path('homepage',views.homepage),
    path('dbitemdisp',views.dbitemdis),
    path('details/<str:pid>',views.product),
    path("addtocart",views.addToCart),
    path("viewcart",views.viewcart),
    path("jgetda",views.jgetdata),
    path("prodsearch",views.prosearch),
    path("search",views.getdata),
    path("pricechart",views.priceChart),
    path("contain/<str:keyword>",views.getdata)
]