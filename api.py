__author__ = "Thimo, Koen, Remon en Edo"
__copyright__ = "Copyright 2016, Groep 4 HU"
__credits__ = ["Nederlandse Spoorwegen", "Hogeschool Utrecht", "Skinkie"]
__license__ = "GNU GPL"
__version__ = "0.75"

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

def stationsindict():
    xml = open('stations.xml', 'r')
    xml_data = xml.read()
    return xmltodict.parse(xml_data)

def check(station):
    if station in stations_lijst:
        return True
    else:
        return False

stations_xml()
vertrektijden('Gouda')
dict = stationsindict()
stations_lijst = []
for station in dict['Stations']['Station']:
    stations_lijst.append(station['Namen']['Lang'])
