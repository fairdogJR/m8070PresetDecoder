
# This script will parse and dump the instrument settings for m8070B setups
#test commit

import os
import xml.etree.cElementTree as ET


print("##############################")
print("########Utility##############")
print("#M8070B preset reader/decoder#")
print("###### Version 1.0 ###########")
print("###Feb 10 2021 Tim Fairfield##")
print("##############################")


#location=input (" enter location of preset folder: ")



location=(r'C:\Users\fairfiel.KEYSIGHT\Documents\Keysight\M8070B\Workspaces\Default\User\Settings\sw_fw_mfiles\pcie1_rx')
print ('example of location of preset files: ')
print (location)
print(" ")

while True:
    location=input (" enter location of your desired preset folder: ")
    file=location+'\InstrumentState.xml'
    print("file= ",file)


    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(file, parser=parser)
    #print(ET.tostring(tree.getroot()))

    root=(tree.getroot())
    # locate plugin names of interest

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

    x=input('<Copy and paste this wherever or Press Enter to go again>')
