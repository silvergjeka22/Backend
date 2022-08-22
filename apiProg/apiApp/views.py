from django.shortcuts import render
from django.http import JsonResponse

# our framework will automatically look for a template called apiOverview.html
from rest_framework.decorators import api_view
from rest_framework.response import Response

# serializers import 
from .serializers import dipendenteSerializer, lavoratoreSerializer, lavoroSerializer, esperienzaSerializer, backup_personSerializer

#import models
from .models import dipendente, lavoratore, lavoro, esperienza, backup_person

# Dipendente API ----------------------------------------------

@api_view(['GET'])
def apiOverviewDipendente(request):
    api_urls = {
        # Dipendente parte
        'List': '/dipendenteList/',
        'Detail View': '/dipendenteDetail/<str:pk>/',
        'Create': '/dipendenteCreate/',
        'Update': '/dipendenteUpdate/<str:pk>/',
        'Delete': '/dipendenteDelete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def dipendenteList(request):

    dipendentes = dipendente.objects.all().order_by('-id')
    serializer = dipendenteSerializer(dipendentes, many=True) # many=True perchè ci sono più dipendenti

    return Response(serializer.data)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def dipendenteDetail(request, pk):

    dipendentes = dipendente.objects.get(id=pk) # pk possimo mettere quello che ogliamo in questo caso ho messo id ma potra essere nome ...
    serializer = dipendenteSerializer(dipendentes, many=False) # False perchè prendo solo 1 dipendente 

    return Response(serializer.data)

@api_view(['POST']) # decorator per indicare che questa funzione è una view
def dipendenteCreate(request):

    serializer = dipendenteSerializer(data=request.data) # data è una variabile che contiene i dati che vengono passati dal client
    
    if serializer.is_valid():
        serializer.save() # salva i dati nel database

    return Response(serializer.data)


@api_view(['POST']) # decorator per indicare che questa funzione è una view
def dipendenteUpdate(request, pk):

    dipendentes = dipendente.objects.get(id=pk)
    serializer = dipendenteSerializer(instance=dipendentes, data=request.data) # instance è una variabile che contiene i dati che vengono passati dal client, data è una variabile che contiene i dati che vengono passati dal client

    if serializer.is_valid():
        serializer.save() # salva i dati nel database

    return Response(serializer.data)



@api_view(['DELETE']) # decorator per indicare che questa funzione è una view
def dipendenteDelete(request, pk):

    dipendentes = dipendente.objects.get(id=pk)
    dipendentes.delete() # cancella i dati nel database
    
    return Response('Item succesfully deleted!')

#Fine Dipendente API ----------------------------------------------






# Lavoratore API ----------------------------------------------

@api_view(['GET'])
def apiOverviewLavoratore(request):
    api_urls = {
        # lavoratore parte
        'List': '/lavoratoreList/',
        'Detail View': '/lavoratoreDetail/<str:pk>/',
        'Create': '/lavoratoreCreate/',
        'Update': '/lavoratoreUpdate/<str:pk>/',
        'Delete': '/lavoratoreDelete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def lavoratoreList(request):

    lavoratores = lavoratore.objects.all().order_by('-id')
    serializer = lavoratoreSerializer(lavoratores, many=True) # many=True perchè ci sono più lavoratori

    return Response(serializer.data)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def lavoratoreDetail(request, pk):

    lavoratores = lavoratore.objects.get(id=pk) # pk possimo mettere quello che ogliamo in questo caso ho messo id ma potra essere nome ...
    serializer = lavoratoreSerializer(lavoratores, many=False) # False perchè prendo solo 1 dipendente 

    return Response(serializer.data)

@api_view(['POST']) # decorator per indicare che questa funzione è una view
def lavoratoreCreate(request):

    serializer = lavoratoreSerializer(data=request.data) # data è una variabile che contiene i dati che vengono passati dal client
    
    if serializer.is_valid():
        serializer.save() # salva i dati nel database

    return Response(serializer.data)


@api_view(['POST']) # decorator per indicare che questa funzione è una view
def lavoratoreUpdate(request, pk):

    lavoratores = lavoratore.objects.get(id=pk)
    serializer = lavoratoreSerializer(instance=lavoratores, data=request.data) # instance è una variabile che contiene i dati che vengono passati dal client, data è una variabile che contiene i dati che vengono passati dal client

    if serializer.is_valid():
        serializer.save() # salva i dati nel database

    return Response(serializer.data)



@api_view(['DELETE']) # decorator per indicare che questa funzione è una view
def lavoratoreDelete(request, pk):

    lavoratores = dipendente.objects.get(id=pk)
    lavoratores.delete() # cancella i dati nel database
    
    return Response('Item succesfully deleted!')


#Fine Lavoratore API ----------------------------------------------


# lavoro API ----------------------------------------------

@api_view(['GET'])
def apiOverviewLavoro(request):
    api_urls = {
        # lavoro parte
        'List': '/lavoroList/',
        'Detail View': '/lavoroDetail/<str:pk>/',
        'Create': '/lavoroCreate/',
        'Update': '/lavoroUpdate/<str:pk>/',
        'Delete': '/lavoroDelete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def lavoroList(request):
    
        lavoros = lavoro.objects.all().order_by('-id')
        serializer = lavoroSerializer(lavoros, many=True)

        return Response(serializer.data)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def lavoroDetail(request, pk):
    
        lavoros = lavoro.objects.get(id=pk)
        serializer = lavoroSerializer(lavoros, many=False)
    
        return Response(serializer.data)


@api_view(['POST']) # decorator per indicare che questa funzione è una view
def lavoroCreate(request):
    
        serializer = lavoroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)


@api_view(['POST']) # decorator per indicare che questa funzione è una view
def lavoroUpdate(request, pk):
        
            lavoros = lavoro.objects.get(id=pk)
            serializer = lavoroSerializer(instance=lavoros, data=request.data)
    
            if serializer.is_valid():
                serializer.save()
            
            return Response(serializer.data)


@api_view(['DELETE']) # decorator per indicare che questa funzione è una view
def lavoroDelete(request, pk):
        
                lavoros = lavoro.objects.get(id=pk)
                lavoros.delete()
                
                return Response('Item succesfully deleted!')


#Fine lavoro API ----------------------------------------------


# esperienza  API ----------------------------------------------

@api_view(['GET'])
def apiOverviewEsperienza(request):
    api_urls = {
        # esperienza parte
        'List': '/esperienzaList/',
        'Detail View': '/esperienzaDetail/<str:pk>/',
        'Create': '/esperienzaCreate/',
        'Update': '/esperienzaUpdate/<str:pk>/',
        'Delete': '/esperienzaDelete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def esperienzaList(request):
        
            esperienzas = esperienza.objects.all().order_by('-id')
            serializer = esperienzaSerializer(esperienzas, many=True)
    
            return Response(serializer.data)
    
@api_view(['GET']) # decorator per indicare che questa funzione è una view
def esperienzaDetail(request, pk):

            esperienzas = esperienza.objects.get(id=pk)
            serializer = esperienzaSerializer(esperienzas, many=False)
    
            return Response(serializer.data)


@api_view(['POST']) # decorator per indicare che questa funzione è una view
def esperienzaCreate(request):
            
                serializer = esperienzaSerializer(data=request.data)
            
                if serializer.is_valid():
                    serializer.save()
                
                return Response(serializer.data)


@api_view(['POST']) # decorator per indicare che questa funzione è una view
def esperienzaUpdate(request, pk):
                
                        esperienzas = esperienza.objects.get(id=pk)
                        serializer = esperienzaSerializer(instance=esperienzas, data=request.data)
                
                        if serializer.is_valid():
                            serializer.save()
                    
                        return Response(serializer.data)    


@api_view(['DELETE']) # decorator per indicare che questa funzione è una view
def esperienzaDelete(request, pk):
                    
                            esperienzas = esperienza.objects.get(id=pk)
                            esperienzas.delete()
                            
                            return Response('Item succesfully deleted!') 


#Fine esperienza API ----------------------------------------------

# backup_person  API ----------------------------------------------

@api_view(['GET'])
def apiOverviewBackupPerson(request):
    api_urls = {
        # backup_person parte
        'List': '/backup_personList/',
        'Detail View': '/backup_personDetail/<str:pk>/',
        'Create': '/backup_personCreate/',
        'Update': '/backup_personUpdate/<str:pk>/',
        'Delete': '/backup_personDelete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET']) # decorator per indicare che questa funzione è una view
def backup_personList(request):
            
                backup_persons = backup_person.objects.all().order_by('-id')
                serializer = backup_personSerializer(backup_persons, many=True)
        
                return Response(serializer.data)  
    

@api_view(['GET']) # decorator per indicare che questa funzione è una view
def backup_personDetail(request, pk):
                
                    backup_persons = backup_person.objects.get(id=pk)
                    serializer = backup_personSerializer(backup_persons, many=False)
            
                    return Response(serializer.data)


@api_view(['POST']) # decorator per indicare che questa funzione è una view
def backup_personCreate(request):
                            
                                serializer = backup_personSerializer(data=request.data)
                            
                                if serializer.is_valid():
                                    serializer.save()
                                
                                return Response(serializer.data)
            

@api_view(['POST']) # decorator per indicare che questa funzione è una view
def backup_personUpdate(request, pk):
                                    
            backup_persons = backup_person.objects.get(id=pk)
            serializer = backup_personSerializer(instance=backup_persons, data=request.data)
                                    
            if serializer.is_valid():
               serializer.save()
                                            
            return Response(serializer.data)


@api_view(['DELETE']) # decorator per indicare che questa funzione è una view
def backup_personDelete(request, pk):
                                            
            backup_persons = backup_person.objects.get(id=pk)
            backup_persons.delete()
                                                    
            return Response('Item succesfully deleted!')

#Fine backup_person API ----------------------------------------------

