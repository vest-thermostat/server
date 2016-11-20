from django.db import models
from django.contrib.auth.models import User

class VestUser(User):
    """
    """
    def __init__(self):
        super().__init__()
