from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Garage, Log, Plaat
import pickle

from django.template.loader import render_to_string
import datetime 
from django.utils import timezone


class HomePageView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        garage = Garage.objects.latest('tijd_her')
        print(garage.plaat)
        return render(request, 'index.html', {'garage':garage})

    
  


def garage_list(request):
    plaat = Garage.objects.all()
    print(plaat)
    return render(request,'index.html', {'plaat': plaat})



class AboutPageView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        logs = Log.objects.all()
    
        over  = [""]
        j = 0
        
        myArr = {}
        BIG = []
        
 
        for e in logs:
            print(e.plaat_id)

           
            

            nr_plaat = Plaat.objects.filter(id = e.plaat_id)
            global log
            log = e
            nu = datetime.datetime.now(timezone.utc)
            tijd =  nu - e.tijd_in
            over.append(tijd)
            print(j)
            j = j + 1

            

         
            for i in nr_plaat:
                print(i.nummerplaat)
                global nummerplaat
                nummerplaat = i.nummerplaat
            
            myArr["nummerplaat"] = nummerplaat

            myArr["tijd_in"] = e.tijd_in
            print(myArr["tijd_in"])

            myArr["tijd_over"] = tijd

            BIG.insert(myArr)
        
        for x in BIG:
            print(x["tijd_in"])


            
           
       
        return render(request, self.template_name, {'log' : logs, 'plaat' : nr_plaat , 'over' : over, 'teller':j, "BIG" : BIG})


class obj(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value 
  

# Add this view
class DataPageView(TemplateView):
    def get(self, request, **kwargs):


        context = {
            'data': [
                {
            
                }
            ]
        }
        

        return render(request, 'data.html', context)
