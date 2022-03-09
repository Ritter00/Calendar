from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date

from .models import BaseRegisterForm, Note
from .forms import NoteForm
from .utils import Calendar

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


class NoteCreate(LoginRequiredMixin, CreateView):
    form_class = NoteForm
    template_name = 'note_create.html'

    def form_valid(self, form):
        note = form.save(commit=False)
        note.user = self.request.user
        note.save()
        return super().form_valid(form)

def get_now_date(_day):
    if _day:
        year, month = (int(x) for x in _day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

class CalendarView(ListView):
    model = Note
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_now = get_now_date(self.request.GET.get('month', None))
        cal = Calendar(date_now.year, date_now.month)
        cal_html = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(cal_html)
        return context