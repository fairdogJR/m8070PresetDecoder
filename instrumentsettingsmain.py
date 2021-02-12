
# This script will parse and dump the instrument settings for m8070B setups
#test commit

import os
import xml.etree.cElementTree as ET
import argparse

print("###############################")
print("########Utility################")
print("#M8070B preset reader/decoder##")
print("###### Version 1.2 ############")
print("###Feb 12 2021 Tim Fairfield###")
print("###############################")
print("  Type --help option for help  ")


#location=input (" enter location of preset folder: ")
parser = argparse.ArgumentParser(description='Decode Keysight M8070 Setup files. This utility parses the xml setup into comma separated data ')
parser.add_argument('location', help= r'paste path to M8070 InstrumentState.xml file '
                                      r'(for example C:\Users\fairfiel.KEYSIGHT\Documents'
                                      r'\Keysight\M8070B\Workspaces\Default\User\Settings\sw_fw_mfiles\pcie1_rx')
parser.add_argument('-m','--moduleinfo',required=False, action='store_true', help='show module information ')

args = parser.parse_args()
print(args.location)


#location=(r'C:\Users\fairfiel.KEYSIGHT\Documents\Keysight\M8070B\Workspaces\Default\User\Settings\sw_fw_mfiles\pcie1_rx')
#print ('example of location of preset files: ')
location=str( args.location)
print (location)
print(" ")

#while True:
#location=input (" enter location of your desired preset folder: ")
file=location+'\InstrumentState.xml'
print("file= ",file)


parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse(file, parser=parser)
#print(ET.tostring(tree.getroot()))

root=(tree.getroot())
# locate plugin names of interest

if args.moduleinfo:
    a = root.findall('.//{http://www.keysight.com/schemas/M8000/StateCoreSetting}MAL')
    for each in a:
        bdict = each.attrib
        #print(b, " ", end='')
        for key, value in bdict.items():
            #print( value,",",end='')
            print( value)
        for each2 in each:
            print (each2.text)

# x=input('<Press Enter to see settings>')

a = root.findall('.//{http://www.keysight.com/schemas/M8000/StateCoreSetting}Property')
# print (a)
for each in a:
    bdict = each.attrib
    #print(b, " ", end='')
    for key, value in bdict.items():
        print( value,",",end='')
    for each2 in each:
        print (each2.text)

