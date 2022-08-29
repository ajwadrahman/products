"""firstpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from welcome import views
from calculater import views as cview
from blogapi import views as bview
from dishesapi.views import DishesView,DishesDetailView
from productsapi.views import ProductsView,ProductDetailView,ProductModelView,ProductDetailModelView

# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register("v3/myp/products",ProductViewsetView,basename="products")
# router.register("v4/myp/products",ProductModelViewSetView,basename="mproducts")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('goodmorning/',views.GoodmorningView.as_view())
#     path('goodafternoon/',views.goodafternoonView.as_view()),
#     path("greetings/",views.GreetingsView.as_view()),
#     path("operations/add/",cview.Addview.as_view()),
#     path("operetions/sub/",cview.Subview.as_view()),
#     path("operation/mult/",cview.Multview.as_view()),
#     path("operations/count/",cview.Countview.as_view()),
     path("blog/posts/",bview.PostView.as_view()),
     path("blog/posts/<int:pid>",bview.PostidView.as_view()),
     path("myp/products/",ProductsView.as_view()),
     path("myp/products/<int:id>", ProductDetailView.as_view()),
     path("api/v2/products",ProductModelView.as_view()),
     path("api/v3/products/<int:id>",ProductDetailModelView.as_view()),


     path("dis/myd/",DishesView.as_view()),
     path("dis/myd/<int:id>",DishesDetailView.as_view()),
]
