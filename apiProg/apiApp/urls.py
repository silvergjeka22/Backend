from django.urls import path
from . import views

urlpatterns = [
    # Dipendente parte
    path('apiOverviewDipendente/', views.apiOverviewDipendente, name='apiOverviewDipendente'),
    path('dipendenteList/', views.dipendenteList, name='dipendenteList'),
    path('dipendenteDetail/<str:pk>/', views.dipendenteDetail, name='dipendenteDetail'),
    path('dipendenteCreate/', views.dipendenteCreate, name='dipendenteCreate'),
    path('dipendenteUpdate/<str:pk>/', views.dipendenteUpdate, name='dipendenteUpdate'),
    path('dipendenteDelete/<str:pk>/', views.dipendenteDelete, name='dipendenteDelete'),

    # Lavoratore parte
    path('apiOverviewLavoratore/', views.apiOverviewLavoratore, name='apiOverviewLavoratore'),
    path('lavoratoreList/', views.lavoratoreList, name='lavoratoreList'),
    path('lavoratoreDetail/<str:pk>/', views.lavoratoreDetail, name='lavoratoreDetail'),
    path('lavoratoreCreate/', views.lavoratoreCreate, name='lavoratoreCreate'),
    path('lavoratoreUpdate/<str:pk>/', views.lavoratoreUpdate, name='lavoratoreUpdate'),
    path('lavoratoreDelete/<str:pk>/', views.lavoratoreDelete, name='lavoratoreDelete'),

    # Lavoro parte
    path('apiOverviewLavoro/', views.apiOverviewLavoro, name='apiOverviewLavoro'),
    path('lavoroList/', views.lavoroList, name='lavoroList'),
    path('lavoroDetail/<str:pk>/', views.lavoroDetail, name='lavoroDetail'),
    path('lavoroCreate/', views.lavoroCreate, name='lavoroCreate'),
    path('lavoroUpdate/<str:pk>/', views.lavoroUpdate, name='lavoroUpdate'),
    path('lavoroDelete/<str:pk>/', views.lavoroDelete, name='lavoroDelete'),

    # Esperienza parte
    path('apiOverviewEsperienza/', views.apiOverviewEsperienza, name='apiOverviewEsperienza'),
    path('esperienzaList/', views.esperienzaList, name='esperienzaList'),
    path('esperienzaDetail/<str:pk>/', views.esperienzaDetail, name='esperienzaDetail'),
    path('esperienzaCreate/', views.esperienzaCreate, name='esperienzaCreate'),
    path('esperienzaUpdate/<str:pk>/', views.esperienzaUpdate, name='esperienzaUpdate'),
    path('esperienzaDelete/<str:pk>/', views.esperienzaDelete, name='esperienzaDelete'),

    #backup_person
    path('apiOverviewBackupPerson/', views.apiOverviewBackupPerson, name='apiOverviewBackupPerson'),
    path('backup_personList/', views.backup_personList, name='backup_personList'),
    path('backup_personDetail/<str:pk>/', views.backup_personDetail, name='backup_personDetail'),
    path('backup_personCreate/', views.backup_personCreate, name='backup_personCreate'),
    path('backup_personUpdate/<str:pk>/', views.backup_personUpdate, name='backup_personUpdate'),
    path('backup_personDelete/<str:pk>/', views.backup_personDelete, name='backup_personDelete'),

]