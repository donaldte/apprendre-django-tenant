from django.contrib import admin

from django.urls import include, path
from customers.views import home, register_customer

# request.tenant is the tenant object associated with the request
# request.tenant.domain_url is the url of the tenant (tenant.domain)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register', register_customer, name='register_customer'),
]
