# from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import VestUser
from django.contrib.gis import forms


class VestUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = VestUser


class VestUserForm(forms.ModelForm):
    home = forms.PointField(
        required=False,
        widget=forms.OSMWidget(attrs={
            'map_width': 800,
            'map_height': 500,
            'modifiable': True,
        })
    )

    class Meta():
        model = VestUser
        fields = ('email', 'home')
