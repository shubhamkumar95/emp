from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from poll.serializers import QuestionSerializer
from .models import Question
import json


@csrf_exempt
def poll(request):
    if request.method == 'GET':
        # print(type(request, "<class 'django.core.handlers.wsgi.WSGIRequest'>
        # "))
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        # data = JSONParser().parse(request.body)
        data = json.loads(request.body)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,
                                status=status.HTTP_201_CREATED)
        else:
            JsonResponse(serializer.errors,
                         status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def poll_details(request, id):
    try:
        instance = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Given object not found"}, status=status.
                            HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilaizer = QuestionSerializer(instance)
        return JsonResponse(data=serilaizer.data, safe=False)
    elif request.method == 'PUT':
        # For parsing request which is wrong approach
        # data = JSONParser().parse(request)
        # For parsing request.body which is right approach
        # JSONParser().parse can be used in APIViews
        data = json.loads(request.body)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,
                                status=status.HTTP_200_OK)
        else:
            JsonResponse(serializer.errors,
                         status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)