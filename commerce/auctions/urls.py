from django.urls import path
from . import views

app_name = "auctions"
urlpatterns = [
    path('', views.auctions_list, name='auctions_list'),
    path('<slug:category_slug>/',
         views.auctions_list,
         name='auctions_list_by_category'),
    path('<int:id>/<slug:slug>',
         views.auction_detail,
         name='auction_detail'),
]
