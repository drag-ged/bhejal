from django.shortcuts import render
from django.http import JsonResponse

def view_json(request):
    data = {'local_maxima' : 'local_maxima[0].tolist()','image':'image_based64'}

    return JsonResponse(data)