import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from numpy import tile
from .models import Product
# Create your views here.

class ProductView(View) :
    
    def get(self,request):
        id = request.GET.get('id')
        if id :
            print("entered the individual get request in the class method")
            return JsonResponse({"products" : "dummy message"})
        else:
            products = list(Product.objects.all().values())
            print(products)
            return JsonResponse(products,safe=False)

    def post(self,request):
        data = json.loads(request.body)
        print(data)
        title = data['title']
        description = data['description']
        price = data['price']

        new_product = Product.objects.create(title=title,description=description,price=price)
        new_product.save()
        return JsonResponse({"Message":f"{title} product saved successfully"})

    def put(self,request):
        data = json.loads(request.body)
        print(data)
        title = data['title']
        description = data['description']

        new_product = Product.objects.get(title=title)
        new_product.description = description
        new_product.save()
        return JsonResponse({"Message":f"{title} product updated with {description} successfully"})

    def delete(self,request):
        data = json.loads(request.body)
        title = data['title']
        new_product = Product.objects.get(title = title)
        new_product.delete()
        return JsonResponse({"Message":f"{title} product deleted successfully"})


