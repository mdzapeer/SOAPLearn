import random
from datetime import datetime
from zeep import Client
from zeep import xsd
from zeep import Transport
from xml.etree.ElementTree import ElementTree, tostring


def rn1():
    random.seed(int(datetime.now().strftime("%f")) * 1000)
    rn1=random.random() * 1000000000
    return int(rn1)

client = Client('http://10.226.187.29:5954/bme/services/AMSService?WSDL')

messagexml=client.create_message(client.service, 'notify', notifyRequest={'MD5CcheckSum':"", 'NO':rn1(), 'URL':"ftp://UMS:Int_Ums123@10.10.70.200/UMS/VOD/TESTSOAP/testsoap1.xml"})
xml1=tostring(messagexml, encoding="unicode")

print(xml1)
print(client.service.notify(notifyRequest={'MD5CcheckSum':"", 'NO':rn1(), 'URL':"ftp://UMS:Int_Ums123@10.10.70.200/UMS/VOD/TESTSOAP/testsoap1.xml"}))
