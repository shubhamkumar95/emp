from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.


def polls_list(request):
    max_objects = 20
    polls = Question.objects.all()[:max_objects]
    data = {"results": list(polls.values("title", "created_by__username",
                                         "created_at"))}
    return JsonResponse(data, safe=False)


def polls_detail(request, pk):
    poll = get_object_or_404(Question, pk=pk)
    data = {"results": {
        "question": poll.title,
        "created_by": poll.created_by.username,
        "created_at": poll.created_at
    }}
    return JsonResponse(data)

