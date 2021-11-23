import argparse
import requests, json
import sys
from sys import argv
import os



api = "http://ip-api.com/json/"


def iplocation(ip): 



        data = requests.get(api+ip).json()
        sys.stdout.flush()
        
       
        print ("[Ip]:", data['query'])
        print("")
      
        print ( "[Operateur]:", data['isp'])
        print("")
       
        print ("[Organisation]:", data['org'])
        print("")
       
        print ("[Ville]:", data['city'])
        print("")
        print ("[Region]:", data['region'])
        print("")
       
        print ("[Longitude]:", data['lon'])
        print("")
       
        print ("[Latitude]:", data['lat'])
        print("")
        
    
        print ("[Time zone]:", data['timezone'])
        print("")
        
        print ("[Code postal]:", data['zip'])
        print("")

print(iplocation(input("mettre l'ip ici -> ")))
