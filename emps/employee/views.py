from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from rest_framework import viewsets

from .serializers import EmployeeSerializer

# Create your views here.


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer


class MyProfile(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer


class ProfileUpdate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer


def index(request):
    return HttpResponse('Response 200', status=200)


def user_login(request):
    pass


def user_logout(request):
    pass


def success(request):
    pass


class EmployeeDetail(DetailView):
    template_name = 'employee_details.html'
    queryset = User.objects.all()
    context_object_name = 'emp'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)


class EmployeeAdd(CreateView):
    template_name = 'employee_form.html'
    form_class = EmployeeSerializer
    # success_url = '/fooder/show/'


class EmployeeUpdate(UpdateView):
    template_name = 'employee_form.html'
    form_class = EmployeeSerializer

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)


class EmployeeListView(ListView):
    template_name = 'show_employee.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        qs = User.objects.all()
        context.update({
            'employees': qs
        })
        return context

