import random
from datetime import datetime
from zeep import Client
from zeep import xsd
from zeep import Transport
from xml.etree.ElementTree import ElementTree, tostring

#random number function
def rn1():
    random.seed(int(datetime.now().strftime("%f")) * 1000)
    rn1=random.random() * 1000000000
    return int(rn1)
#ID input from user
def getID():
    ID=str(input("\nEnter ID: \n"))
    ID=ID.upper()
    return "ftp://UMS:Int_Ums123@10.10.70.200/UMS/VOD/"+ID+"/"+ID+".xml"


#WSDL URL
client = Client('http://10.226.187.29:5954/bme/services/AMSService?WSDL')

#RAW SOAP message check
messagexml=client.create_message(client.service, 'notify', notifyRequest={'MD5CcheckSum':"", 'NO':rn1(), 'URL':getID()})
xml1=tostring(messagexml, encoding="unicode")
print(xml1)

#POST SOAP message
#print(client.service.notify(notifyRequest={'MD5CcheckSum':"", 'NO':rn1(), 'URL':getID()"}))
