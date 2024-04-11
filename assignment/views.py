import random
from django.shortcuts import render
from myActivity.models import MyActivity
from historyMedicalConsultations.models import HistoryMedicalConsultations
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

def assigment(request):
    if request.method == 'GET':
        assigment_item = MyActivity.objects.all()
        print(assigment_item)
        new_list = []
        for item in assigment_item:
            if str(item.status) == 'Disponible':
                new_list.append(item.doctor)
            else:
                content = {'message': 'Sin servicio'}
        
        insert_item = random.choice(new_list)
        response = HistoryMedicalConsultations(doctor=insert_item, date_start="04 abril 2024: 12:30", date_end="04 abril 2024: 13:00", incidents="Ninguno", user="Antonio")
        response.save()
        content = {'message': 'Ok'}

        return JsonResponse(content)

