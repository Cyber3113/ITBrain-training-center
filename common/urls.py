from rest_framework.routers import DefaultRouter
from app_products import views as product_views

router = DefaultRouter()


router.register('product', product_views.ProductViewSet, basename='product')


urlpatterns = [

              ] + router.urls
