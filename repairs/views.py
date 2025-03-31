from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from repairs.forms import RepairRequestForm

from repairs.models import RepairRequest


class HomeView(FormView):
    template_name = 'index.html'
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


class AdminHomeView(LoginRequiredMixin, ListView):
    model = RepairRequest
    template_name = 'admin/home.html'
    context_object_name = 'requests'
    ordering = ['-created_at']


class MarkProcessedView(View):
    def post(self, request, pk):
        repair_request = get_object_or_404(RepairRequest, pk=pk)
        repair_request.is_processed = True
        repair_request.save()
        return HttpResponse('<span class="badge bg-success">Опрацьовано</span>')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])