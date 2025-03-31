from django.views.generic.edit import FormView
from django.http import HttpResponse
from repairs.forms import RepairRequestForm

class HomeView(FormView):
    template_name = 'home.html'
    form_class = RepairRequestForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        if self.request.htmx:
            return HttpResponse('<div class="alert alert-success">Заявку прийнято!</div>')
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.htmx:
            return HttpResponse('<div class="alert alert-danger">Форма містить помилки.</div>')
        return super().form_invalid(form)
