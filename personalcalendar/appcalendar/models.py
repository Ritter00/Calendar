from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Create your models here.

class BaseRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label="Фамилия")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    complete = models.BooleanField(default=False)
    text = models.TextField()
    start_time = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/note/{self.id}'

    def get_html(self):
        url = f'/note/{self.id}'
        return f'<p><b>{self.start_time.strftime("%H:%M")}</b><a href="{url}"> {self.title} </a></p>'

