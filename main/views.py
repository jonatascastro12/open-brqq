import json
import os

import time
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView
from django_celery_results.models import TaskResult

from main.models import City, GloboVideo
from main.tasks import run_crawler


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/login/'
    redirect_field_name = 'next'
    template_name = 'home_view.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['num_municipios'] = City.objects.count()
        context['num_municipios_com_video'] = City.objects.filter(video__isnull=False).count()
        if context['num_municipios'] > 0:
            context['num_municipios_com_video_pct'] = (context['num_municipios_com_video'] / context[
                'num_municipios']) * 100
        context['num_municipios_com_video_e_legenda'] = City.objects.filter(video__isnull=False,
                                                                            video__subtitle_content__isnull=False).count()
        if context['num_municipios'] > 0:
            context['num_municipios_com_video_e_legenda_pct'] = (context['num_municipios_com_video_e_legenda'] /
                                                                 context['num_municipios']) * 100
        context['num_videos'] = GloboVideo.objects.count()
        context['num_videos_com_legenda'] = GloboVideo.objects.filter(subtitle_content__isnull=False).count()

        context['num_municipios_legenda_tratada'] = City.objects.filter(treated_subtitle_part__isnull=False).count()

        tasks = []
        for t in TaskResult.objects.all().order_by('-id')[:5]:
            try:
                tasks.append(
                    {'id': t.id, 'status': t.status, 'result': json.loads(t.result), 'error': t.traceback,
                     'date_done': t.date_done})
            except:
                pass

        context['tasks'] = tasks

        return context



class DownloadDbView(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    redirect_field_name = 'next'

    def get(self, request, *arg, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404


class RunVideoCrawlerView(LoginRequiredMixin, View):
    login_url = '/admin/login/'
    redirect_field_name = 'next'

    def get(self, request, *arg, **kwargs):
        task = run_crawler.delay()
        # task = run_crawler()

        time.sleep(1)

        return redirect('home')
