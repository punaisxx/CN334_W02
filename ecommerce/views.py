from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import requests

# Create your views here.
def ecommerce_index_view(request):
        '''This function render index page of ecommerce views'''

        return HttpResponse('Welcome to 6410742479 Rawinnipha Thawornniwatsakun views!')

def item_view(request, item_id):

        context_data = {
                "item_id": item_id
        }

        return render(request, 'index.html', context = context_data)

def home_view(request):
        return render(request, 'home.html')

def category_view(request):
        return render(request, 'category.html')

def product_view(request):
        return render(request, 'product.html')

def checkout_view(request):
        return render(request, 'checkout.html')

def contact_view(request):
        return render(request, 'contact.html')

@csrf_exempt
def basic_request(request):
        if request.method == "GET":
                return JsonResponse({"status":"GET Pass"}, safe=False)
        
        if request.method == "POST":
                return JsonResponse({"status":"POST Pass"}, safe=False)
        
@csrf_exempt
def tokenize(request):
  if request.method == "POST":
     try:
        sentence = request.POST['text']
     except:
        return JsonResponse({"error":"Input not found"}, safe=False, status=500)
     url = "https://api.aiforthai.in.th/tlexplus"
     data = {'text':'ข้าวและแป้งมีสารอาหารหลักคือคาร์โบไฮเดรต'}
     headers = {
        'Apikey': "0m4yqogsA9W1W7mCRRNzONnkzsISN82g"
        }
     response = requests.post(url, data=data, headers=headers)
     reponse_json = response.json()
     return JsonResponse({"student":"student_id", "tokenize":reponse_json}, safe=False)
  return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)