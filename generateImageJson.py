# Christian Piper
# 12/2/19
# This file contains the functions and code necessary to build .json files for each of the images based on the .csv or .xml files

import os
import time 

json_file_contents = ""


def getInfoFromXML(xml_file_contents):
    file_name = getXMLValue(xml_file_contents, "filename")
    width = getXMLValue(xml_file_contents, "width")
    height = getXMLValue(xml_file_contents, "height")

    last_tag_index = 0

    object_list = [file_name, width, height]

    run = True

    while run:
        object = getXMLValue(xml_file_contents, "object", start_index = last_tag_index)
        if not (object == -1 or object == None):
            last_tag_index = xml_file_contents.find("</object>", last_tag_index)
            value_namings = ["name", "xmin", "ymin", "xmax", "ymax"]
            for entry in range(0, 5):
                entry_value = getXMLValue(object, value_namings[entry])
                if len(object_list) > 5:
                    if entry_value == object_list[len(object_list) - 5]:
                        run = False
                        break
                if not entry_value == None:
                    object_list.append(entry_value)
                else:
                    run = False
                    break   
        else:
            break
    
    return object_list


def getXMLValue(xml_file_contents, parameter_name, start_index = 0, end_index = -1):
    # If there wasn't an end specified, use the entire length
    if not xml_file_contents == None:
        if end_index == -1:
            end_index = len(xml_file_contents)
        start = xml_file_contents.find("<" + str(parameter_name) + ">", start_index, end_index)
        end = xml_file_contents.find("</" + str(parameter_name) + ">", start_index + 5, end_index)
        if not end == -1:
            characters = xml_file_contents[ start + len(parameter_name) + 2: end ]
        else:
            characters = None
    else:
        print("No objects found")
        characters = None
    return characters


def generateJson(file_name, width, height, names, xmins, ymins, xmaxes, ymaxes):
    global json_file_contents
    json_file_contents = ""

    addString('''{
  "description": "",
  "tags": [],
  "size": {
    "height": ''')
    addString(height)

    addString(''',
    "width": ''')

    addString(width)

    addString('''
  },
  "objects": [''')

    for object_ in range(0, len(xmins)):
        addString('''\n    {
      "description": "",
      "bitmap": null,
      "tags": [],
      "classTitle": "''')

        addString(names[object_])

        addString('''",
      "points": {
        "exterior": [
          [
            ''')

        addString(xmins[object_])

        addString(''',
            ''')

        addString(ymins[object_])

        addString('''
          ],
          [
            ''')

        addString(xmaxes[object_])

        addString(''',
            ''')
        
        addString(ymaxes[object_])

        addString('''
          ]
        ],
        "interior": []
      }
    }''')

        if (len(xmins) - object_) - 1 > 0:
            addString(",")

    
    addString('''
  ]
}''')

    return json_file_contents
    


    

def addString(addition):
    global json_file_contents
    json_file_contents = json_file_contents + str(addition)


XMLFileConstants = '''<annotation verified="yes">
    <folder>Annotation</folder>
    <filename>DSC00303.JPG</filename>
    <path>2018-19-FRC-Vision-Labeling-PascalVOC-export/Annotations/DSC00303.JPG</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>4912</width>
        <height>3264</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
    <name>Tape</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>3733.6819196428573</xmin>
        <ymin>1820.6451612903224</ymin>
        <xmax>3786.3104910714287</xmax>
        <ymax>1908.3870967741934</ymax>
    </bndbox>
</object><object>
    <name>Tape</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>3575.796205357143</xmin>
        <ymin>1807.4838709677417</ymin>
        <xmax>3641.5819196428574</xmax>
        <ymax>1908.3870967741934</ymax>
    </bndbox>
</object><object>
    <name>Hatch</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>4816.953348214286</xmin>
        <ymin>1741.6774193548385</ymin>
        <xmax>4912</xmax>
        <ymax>1961.0322580645159</ymax>
    </bndbox>
</object><object>
    <name>Hatch</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>4838.881919642858</xmin>
        <ymin>1456.516129032258</ymin>
        <xmax>4912.000000000001</xmax>
        <ymax>1702.1935483870968</ymax>
    </bndbox>
</object>
</annotation>
'''
