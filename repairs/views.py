import logging

from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from repairs.forms import RepairRequestForm
from repairs.models import RepairRequest

logger = logging.getLogger(__name__)


class HomeView(FormView):
    template_name = 'index.html'
    form_class = RepairRequestForm
    success_url = '/'

    def form_valid(self, form):
        repair_request = form.save()
        logger.info(f"New repair request created: ID={repair_request.pk}, User={self.request.user}")
        if self.request.htmx:
            return HttpResponse('<div class="alert alert-success">Request submitted successfully!</div>')
        return super().form_valid(form)

    def form_invalid(self, form):
        logger.warning(f"Form submission failed with errors: {form.errors.as_json()}")
        if self.request.htmx:
            return HttpResponse('<div class="alert alert-danger">The form contains errors.</div>')
        return super().form_invalid(form)


class AdminHomeView(LoginRequiredMixin, ListView):
    model = RepairRequest
    template_name = 'admin/home.html'
    context_object_name = 'requests'
    ordering = ['-created_at']

    def get(self, request, *args, **kwargs):
        logger.info(f"Admin panel accessed by user: {request.user}")
        return super().get(request, *args, **kwargs)


class MarkProcessedView(View):
    def post(self, request, pk):
        repair_request = get_object_or_404(RepairRequest, pk=pk)
        repair_request.is_processed = True
        repair_request.save()
        logger.info(f"Repair request ID={pk} marked as processed by user: {request.user}")
        return HttpResponse('<span class="badge bg-success">Processed</span>')

    def get(self, request, *args, **kwargs):
        logger.warning(f"GET request attempted on MarkProcessedView by user: {request.user}")
        return HttpResponseNotAllowed(['POST'])
