from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Garage, Log, Plaat
import mysql.connector
import MySQLdb
from django.template.loader import render_to_string
import datetime 
from django.utils import timezone


class HomePageView(TemplateView):
    template_name = "index.html"
    
  


def garage_list(request):
    plaat = Garage.objects.all()
    print(plaat)
    return render(request,'index.html', {'plaat': plaat})



class AboutPageView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        logs = Log.objects.all()
    
        #plaat_id = Log.objects.values('plaat_id')
        #plaat = Plaat.objects.raw('SELECT id, nummerplaat FROM plaat WHERE id = %s' , [plaat_id])
        #plaat = Plaat.objects.filter(plaat_id = plaat_id).values('nummerplaat')

        #print(plaat)

      
        #nr_plaat = Plaat.objects.filter(id = pl_id)

        #print(plaat_id)

        for e in logs:
            print(e.plaat_id)

            nr_plaat = Plaat.objects.filter(id = e.plaat_id)
            global log
            log = e
            for i in nr_plaat:
                print(i.nummerplaat)
                global nummerplaat
                nummerplaat = i.nummerplaat

                nu = datetime.datetime.now(timezone.utc)

                over = nu - e.tijd_in
                print(over)

       
        return render(request, self.template_name, {'log' : logs, 'plaat' : nr_plaat , 'tijd_over' : over})

  

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
