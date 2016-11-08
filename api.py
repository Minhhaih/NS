import requests
import codecs
import xmltodict

username = 'thimo@vodafonethuis.nl'
password = 'yIrAgJtY95pNSMXcBhSMaqtnrs29TajakBsU482dxeO4SvGfR1ZCXg'

url = 'http://webservices.ns.nl/ns-api-stations-v2'

def vertrektijden(station):
    url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
    data = requests.get(url, auth = (username, password))
    xml = codecs.open('vertrektijden.xml', "w", "utf-8")
    xml.write(str(data.text))
    xml.close()
    return xmltodict.parse(data.text)

def stations_xml():
    data = requests.get(url, auth = (username, password))
    xml = codecs.open('stations.xml', "w", "utf-8")
    xml.write(str(data.text))
    xml.close()

stations_xml()
vertrektijden('Gouda')
