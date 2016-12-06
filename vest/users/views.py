from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from users.forms import VestUserCreationForm
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

class UserEdit():
    pass

class Login():
    pass
