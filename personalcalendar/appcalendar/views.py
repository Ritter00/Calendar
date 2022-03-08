from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe

# Create your views here.

class MyView(TemplateView):
    template_name = 'default.html'


class MyViewReq(LoginRequiredMixin, TemplateView):
    template_name = 'req.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cl = HTMLCalendar(firstweekday=0)
        context['cal'] = mark_safe(cl.formatmonth(2020, 5))
        return context


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/login/'