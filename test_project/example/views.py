from django.shortcuts import render
from django.views.generic import TemplateView, ListView
import pymysql
from .models import Garage
import mysql.connector
import MySQLdb
from django.template.loader import render_to_string


mydb = mysql.connector.connect(
  host="localhost",
  user="plates",
  passwd="CelineKdG1234+",
  database="plates"
)

mycursor = mydb.cursor()



class HomePageView(TemplateView):
    template_name = "index.html"
    def get_queryset(self):
        return Garage.objects.all()


def garage_list(request):
    db = MySQLdb.connect(host='localhost',  port=3306 ,user='plates', db="plates", passwd='CelineKdG1234+')
    cursor=db.cursor()
    cursor.execute('SELECT plaat FROM garage')
    result = cursor.fetchall()
    plaat =  result[0]

    
    
    return render_to_string('index.html', {'plaat', plaat})

    db.close()


class AboutPageView(TemplateView):
    template_name = "about.html"

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