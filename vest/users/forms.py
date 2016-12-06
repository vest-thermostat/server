from django.contrib.auth.forms import UserCreationForm
from users.models import VestUser


class VestUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = VestUser
