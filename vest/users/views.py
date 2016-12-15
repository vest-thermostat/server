from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer

from users.permissions import IsSelf
from users.serializers import UserSerializer
from users.forms import VestUserCreationForm, VestUserForm
from users.models import VestUser

class Registration(CreateView):
    template_name = 'register.html'
    form_class = VestUserCreationForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(Registration, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class UserEditView(UpdateView):
    model = VestUser
    template_name = "edit.html"
    form_class = VestUserForm

    def get_object(self, queryset=None):
        return self.request.user


class UserProfileView(viewsets.ModelViewSet):
    queryset = VestUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsSelf,
    )
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "profile.html"
