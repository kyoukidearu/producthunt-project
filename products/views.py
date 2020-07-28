from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):
    if request.method == 'POST':

        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST['icon'] and request.POST['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'https://' + request.POST['url']
            product.icon = request.POST['icon']
            product.image = request.POST['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()  # this inserts into db
            return redirect('home')  # placeholder until code to direct to product page
        else:
            return render(request, 'products/create.html', {'error':'All fields are required'})

    else:
        return render(request, 'products/create.html')
