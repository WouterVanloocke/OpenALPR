#!/usr/bin/env python
import numpy as np
import cv2
import sys
import subprocess
import mysql.connector
from openalpr import Alpr


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="plate",
  database="plates"
)

#subprocess.call("/home/wouter/FlaskApp/app.py", shell=True)

mycursor = mydb.cursor()


platevalues=[""]
WINDOW_NAME  = 'openalpr'
FRAME_SKIP = 30

alpr = Alpr("eu", "/etc/openalpr/openalpr.conf", "openalpr/runtime_data/")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
    
alpr.set_top_n(20)


#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('filmpje.avi')
if not cap.isOpened():
   alpr.unload()
   sys.exit('Failed to open video file!')
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
cv2.setWindowTitle(WINDOW_NAME, 'OpenALPR video test')

_frame_number = 0
f = open("data.txt", "w")
while True:
      ret_val, frame = cap.read()

      _frame_number += 1
      if _frame_number % FRAME_SKIP != 0:
         cv2.imshow(WINDOW_NAME, frame)

      results = alpr.recognize_ndarray(frame)
      for i, plate in enumerate(results['results']):
          best_candidate = plate['candidates'][0]
          #print ('Plate #{}: {:7s} ({:.2f}%)'.format(i, best_candidate['plate'].upper(), best_candidate['confidence']))
          if (best_candidate['confidence'] > 89):
               platevalues.append(best_candidate['plate'])
               if (platevalues.count(best_candidate['plate']) == 2):
          #if (best_candidate['confidence']) > 93:
                   x = best_candidate['plate']
                   print ('Plate #{}: {:7s} ({:.2f}%)'.format(i, best_candidate['plate'].upper(), best_candidate['confidence']))
                   #print(best_candidate['plate'].upper())
                  #  plaat = best_candidate['plate'].upper()
                  #  mycursor.execute("SELECT nummerplaat,eigenaar_id FROM plaat")
                  #  myresult = mycursor.fetchall()
                  #  for row in myresult:
                  #     if (row[0] == plaat):
                  #       print(plaat + " en " +row[0] + " komen wel overeen")
                  #       mycursor.execute("""SELECT medewerkers.voornaam AS voornaam, medewerkers.achternaam AS achternaam FROM medewerkers INNER JOIN plaat ON medewerkers.id = plaat.eigenaar_id AND medewerkers.id ='%s'""" % (row[1]))
                  #       result = myresult = mycursor.fetchall()
                  #       for rij in result:
                  #           print(rij[0]+" "+rij[1]+" mag doorrijden!")
                  #           print("")
                  #     if not (row[0] == plaat): 
                  #       print(plaat + " en " +row[0] + " komen niet overeen")
                  #       mycursor.execute("""SELECT medewerkers.voornaam AS voornaam, medewerkers.achternaam AS achternaam  FROM medewerkers INNER JOIN plaat ON medewerkers.id = plaat.eigenaar_id AND medewerkers.id ='%s'""" % (row[1]))
                  #       result = myresult = mycursor.fetchall()
                  #       for r in result:
                  #           print(r[0]+" "+r[1]+" mag niet binnen!") 
                  #           print("")
      if cv2.waitKey(1) == 27:
          break
f.close()
cv2.destroyAllWindows()
cap.release()
alpr.unload()

if __name__ == '__main__':
   app.run(debug=True)
