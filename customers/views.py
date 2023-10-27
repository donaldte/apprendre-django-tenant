from django.shortcuts import render
from django.contrib import messages
from datetime import datetime, timedelta
# Create your views here.
from .models import Client, Domain

def home(request, *args, **kwargs):
    return render(request, 'home.html', {})



def register_customer(request, *args, **kwargs):
    if request.method == 'POST':
        pays = request.POST.get('pays')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        institution_name = request.POST.get('institution_name')
        
        if password != password2:
            messages.success(request, 'Passwords does\'t match')
            return render(request, 'register_customer.html', {})
        
        number = Client.objects.count() 
        
        tenant = Client.objects.create(
            schema_name=f'tenant{number}',  # test
            name=institution_name,
            paid_until=datetime.now() + timedelta(days=13),
            on_trial=True
        )  
        
        # form client domain 
        
        dom = "{}.{}".format(tenant.schema_name, request.get_host().split(':')[0])
        domain = Domain()
        domain.domain = dom
        domain.tenant = tenant
        domain.is_primary = True
        domain.save()
        
        # messages success
        
        host = request.get_host()
        
        http_protocol = request.scheme
        
        connection_url = f'{http_protocol}://{tenant.schema_name}.{host}'
        return render(request, 'register_customer.html', {'url': connection_url})
    return render(request, 'register_customer.html', {})
