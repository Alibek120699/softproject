import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show_projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer =
