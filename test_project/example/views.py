from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Garage, Log, Plaat, Eigenaar, Medewerkers


from django.template.loader import render_to_string
import datetime 
from django.utils import timezone


class HomePageView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        garage = Garage.objects.latest('tijd_her')
        print(garage.plaat)
        print(garage.plaat_id)

        plaat = Plaat.objects.get(id = garage.plaat_id)
        print(plaat.eigenaar_id)

        eigenaar = Eigenaar.objects.get(id = plaat.eigenaar_id)
        print(eigenaar.voornaam)

        toegang = ""

        if plaat.actief == 1:
            print("actief")
            toegang = "access"
            photo = 'access.png'
        elif plaat.actief == 0:
            
            toegang = "no access"
            photo = 'noaccess.png'

        return render(request, 'index.html', {'garage':garage , 'access':toegang, 'eigenaar' : eigenaar, 'photo' : photo})

    
    def post(self, request):
        post = request.POST.get("plaat", "")
        plaatid = Plaat.objects.get(nummerplaat = post)
        medewerkers = Medewerkers.objects.filter(id = plaatid.eigenaar_id).values()
        return render(request, 'data.html', {'medewerkers':medewerkers})
        


    
  


def garage_list(request):
    plaat = Garage.objects.all()
    print(plaat)
    return render(request,'index.html', {'plaat': plaat})



class AboutPageView(TemplateView):
    template_name = "about.html"

    def get(self, request):
        logs = Log.objects.all()
        platen = []
        tijden = []
        nu = datetime.datetime.now(timezone.utc)
        #plaat_id = Log.objects.values('plaat_id')
        #plaat = Plaat.objects.raw('SELECT id, nummerplaat FROM plaat WHERE id = %s' , [plaat_id])
        #plaat = Plaat.objects.filter(plaat_id = plaat_id).values('nummerplaat')

        #print(plaat)

      
        #nr_plaat = Plaat.objects.filter(id = pl_id)

        #print(plaat_id)

       # for e in logs:
          #  print(e.plaat_id)
        for i in logs:
           nr_plaat = Plaat.objects.get(id = i.plaat_id)
           over = nu - i.tijd_in
           tijden.append(over)
          # print(nr_plaat.nummerplaat)
           platen.append(nr_plaat.nummerplaat)
        return render(request, self.template_name, {'combo' : zip(logs,platen,tijden)})



# Add this view
class DataPageView(TemplateView):
    def get(self, request, **kwargs):
       template_name = "data.html"

    def get(self, request):
        medewerkers = Medewerkers.objects.all()
        print(medewerkers)
        return render(request, 'data.html', {'medewerkers':medewerkers})

    def post(self, request):
        post = request.POST.get("plaat", "")
        plaatid = Plaat.objects.get(nummerplaat = post)
        medewerkers = Medewerkers.objects.filter(id = plaatid.eigenaar_id).values()
        return render(request, 'data.html', {'medewerkers':medewerkers})