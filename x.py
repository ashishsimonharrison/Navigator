import re
from Tkinter import *
import json, urllib
from urllib import urlencode
import googlemaps
root=Tk()
global root2
root2=Tk()

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


def num():
  root2.destroy();


root.title('Navigator')
root2.title('Directions')


def number():
    
    #print(start)
    #print(finish)
    start=e1.get()
    finish=e2.get()
    url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((('origin',start),('destination',finish)))
    ur = urllib.urlopen(url)
    
    result = json.load(ur)
    y=''
    
    #w.delete()
    try:
     for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
          j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
          #textbox.insert(END,cleanhtml(j)+'\n')
          #print(textbox.get(1.0,END))
          w=Label(root2,text=cleanhtml(j))
          w.pack()
     root.destroy()
    except:
     #textbox.insert(END,"ENTER A VALID ADDRESS")
      w=Label(root2,text='ENTER A VALID ADDRESS')
      w.pack()
      root.destroy()

         
button_1 = Button(root, text="Start...", command=number)
button_1.grid(row=4)
'''button_2=Button(root2, text="Exit", command=fr)
button_2.grid(row=1)
#textbox = Text(root2)
#textbox.grid(row=0)'''



Label(root, text="Start Address").grid(row=0)
Label(root, text="End Address").grid(row=1)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
root.mainloop()
root2.mainloop()
  
