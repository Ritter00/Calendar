from calendar import HTMLCalendar
from .models import Note, User

class Calendar(HTMLCalendar):
     def __init__(self, year=None, month=None, user_id=None):
         self.year = year
         self.month = month
         self.user_id = user_id
         super(Calendar, self).__init__()

     def formatday(self, day, notes):
         user = User.objects.get(id=self.user_id)
         note_day = notes.filter(start_time__day=day, user=user)
         add_html = ''
         for note in note_day:
             add_html += f'<li>{note.get_html()}</li>'
         if day != 0:
             return f"<td><span class='date'>{day}</span><ul> {add_html} </ul></td>"
         return '<td></td>'

     def formatweek(self, theweek, notes):
         week = ''
         for d, weekday in theweek:
             week += self.formatday(d, notes)

         return f'<tr>{week}</tr>'

     def formatmonth(self, withyear=True):
         notes = Note.objects.filter(start_time__year=self.year, start_time__month=self.month)
         cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
         cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
         cal += f'{self.formatweekheader()}\n'
         for week in self.monthdays2calendar(self.year, self.month):
             cal += f'{self.formatweek(week, notes)}\n'
         return cal