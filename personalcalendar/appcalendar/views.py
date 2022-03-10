from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.utils.safestring import mark_safe
from datetime import datetime, date


from .models import BaseRegisterForm, Note
from .forms import NoteForm
from .utils import Calendar


class MyView(TemplateView):
    template_name = 'default.html'


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


class CalendarView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'calendar.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.request.user.id
        date_now = get_now_date(self.request.GET.get('month', None))
        cal = Calendar(date_now.year, date_now.month, id_user)
        cal_html = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(cal_html)
        context['name']= User.objects.get(id=id_user)
        return context


class NoteDetail(LoginRequiredMixin, DetailView):
    template_name = 'note_detail.html'
    model = Note

    def get_queryset(self):
        user = self.request.user
        q = super().get_queryset()
        return q.filter(user=user)


