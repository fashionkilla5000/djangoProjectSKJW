from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from .api.serializers import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ZolnierzListView(ListView):
    model = Zolnierz
    template_name = 'zolnierze/zolnierze_list.html'


class ZolnierzDetailView(DetailView):
    model = Zolnierz
    template_name = 'zolnierze/zolnierze_detail.html'


class KontraktyListView(ListView):
    model = Kontrakty
    template_name = 'zolnierze/zolnierze_list.html'


class KontraktyDetailView(DetailView):
    model = Kontrakty
    template_name = 'zolnierze/zolnierze_detail.html'



class PrzepustkiListView(ListView):
    model = Przepustki
    template_name = 'zolnierze/zolnierze_list.html'


class PrzepustkiDetailView(DetailView):
    model = Przepustki
    template_name = 'zolnierze/zolnierze_detail.html'


class WnioskiListView(ListView):
    model = Wnioski
    template_name = 'zolnierze/zolnierze_list.html'


class WnioskiDetailView(DetailView):
    model = Wnioski
    template_name = 'zolnierze/zolnierze_detail.html'

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
