from django.core.urlresolvers import reverse
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, logout, authenticate
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

    # class Meta:
    #     model = VestUser


# class Login(auth_views.login):
#     template_name = 'register.html'
#     success_url = '/'


class UserProfileView(DetailView):
    pass

class UserEditView(UpdateView):
    model = VestUser
    template_name = "edit.html"
    form_class = VestUserForm

    def get_absolute_url(self):
        return reverse('profile')

    # def form_valid(self, form):
    #     valid = super(Registration, self).form_valid(form)
    #     print("IS VALID ???? : " + str(valid))
    #     return valid

    def get_object(self, queryset=None):
        return self.request.user
