#from .models import User
from django.http import (HttpResponse, HttpResponseBadRequest, JsonResponse)
from django.core import serializers
import json
from books.models import User
from rest_framework.decorators import api_view


def index(request):
    # people = User.objects.all()

    # tmpJson = serializers.serialize("json", people)
    # tmpObj = json.loads(tmpJson)

    print('tmpJson')

    # return HttpResponse(json.dumps(tmpObj), content_type="application/json", headers={"Access-Control-Allow-Origin": "http://localhost:3000", "Access-Control-Allow-Credentials": "true", "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT, PATCH", "Access-Control-Allow-Headers": "Origin, Content-Type, Accept"})

@api_view(['POST'])
def create_user(request):
    # name=request.POST.get('name', False)
    # email=request.POST.get('email', False)
    # password=request.POST.get('password', False)

    mydata = json.loads(request.body.decode("utf-8"))

    isExist = User.objects.filter(email = mydata['email']).exists()

    if (isExist):
        return HttpResponseBadRequest("Некорректные данные")
    else:
        user = User.objects.create_user(mydata['email'], mydata['name'], mydata['password'])

        return JsonResponse({}, content_type="application/json", headers={"Access-Control-Allow-Origin": "http://localhost:3000", "Access-Control-Allow-Credentials": "true", "Access-Control-Allow-Methods": "GET, POST, OPTIONS, PUT, PATCH", "Access-Control-Allow-Headers": "Origin, Content-Type, Accept"})
