from django.conf.urls import url
from app import views
from django.conf import settings
from django.contrib.auth import logout
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url(r'^workers/$', views.workers, name="workers"),
                  url(r'^nocomp/$', views.nocomp, name="nocomp"),
                  # company
                  url(r'^add/company/', views.add_company, name="add_company"),
                  # farm
                  url(r'^add/farm/', views.add_farm, name="add_farm"),
                  url(r'^farm/(?P<pk>[0-9]+)/$', views.farm_details, name="farm_details"),
                  url(r'^farm/(?P<pk>[0-9]+)/delete/$', views.farm_delete, name="farm_delete"),
                  url(r'^farm/(?P<pk>[0-9]+)/update/$', views.FarmUpdate.as_view(), name="farm_update"),
                  # jobs
                  url(r'^jobs/add$', views.jobs_add, name="jobs_add"),
                  url(r'^job/(?P<pk>[0-9]+)/delete/$', views.job_delete, name="job_delete"),
                  url(r'^job/(?P<pk>[0-9]+)/update/$', views.JobUpdate.as_view(success_url="/jobs/add"),
                      name="job_update"),
                  # workers
                  url(r'^workers/add$', views.workers_add, name="workers_add"),
                  url(r'^worker/(?P<pk>[0-9]+)/details/$', views.worker_details, name="worker_details"),
                  url(r'^worker/(?P<pk>[0-9]+)/delete/$', views.worker_delete, name="worker_delete"),
                  url(r'^worker/(?P<pk>[0-9]+)/update/$', views.WorkerUpdate.as_view(), name="worker_update"),
                  url(r'^worker/(?P<pk>[0-9]+)/archive/$', views.worker_archive, name="worker_archive"),
                  url(r'^worker/old/$', views.old_workers, name="old_workers"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
