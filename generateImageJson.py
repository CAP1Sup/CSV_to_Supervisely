# Christian Piper
# 12/2/19
# This file contains the functions and code necessary to build .json files for each of the images based on the .csv or .xml files

import os

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
        if not object == -1:
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
    if end_index == -1:
        end_index = len(xml_file_contents)
    start = xml_file_contents.find("<" + str(parameter_name) + ">", start_index, end_index)
    end = xml_file_contents.find("</" + str(parameter_name) + ">", start_index + 5, end_index)
    if not end == -1:
        characters = xml_file_contents[ start + len(parameter_name) + 2: end ]
    else:
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
    <filename>DSC00296.JPG</filename>
    <path>2018-19-FRC-Vision-Labeling-PascalVOC-export/Annotations/DSC00296.JPG</path>
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
    <name>Ball</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>0</xmin>
        <ymin>1706.5806451612902</ymin>
        <xmax>832.5319196428572</xmax>
        <ymax>3264</ymax>
    </bndbox>
</object><object>
    <name>Hatch</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <bndbox>
        <xmin>586.9319196428572</xmin>
        <ymin>636.1290322580645</ymin>
        <xmax>2047.3747767857144</xmax>
        <ymax>3263.9999999999995</ymax>
    </bndbox>
</object>
</annotation>
'''

# getInfoFromXML(XMLFileConstants)\
width = 4912
height = 3264
names = ["ball", "hatch"]
xmins = [581, 0]
ymins = [645, 3264]
xmaxes = [2058, 810]
ymaxes = [3258, 1714]

generateJson("test.jpeg", width, height, names, xmins, ymins, xmaxes, ymaxes)