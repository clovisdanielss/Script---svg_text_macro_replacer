from xml.dom import minidom
import sys

variables = {
    "#num_ticket1": "Nº 001",
    "#num_ticket2": "Nº 002",
    "#num_ticket3": "Nº 003",
    "#num_ticket4": "Nº 004",
    "#num_ticket5": "Nº 005",
    }

def replace_variables(elements):
    for ele in elements:
        if ele.firstChild != None and ele.firstChild.nodeType == ele.TEXT_NODE and ele.firstChild.nodeValue in variables.keys():
            ele.firstChild.replaceWholeText(variables[ele.firstChild.nodeValue])
            print(ele.firstChild.nodeValue)

def custom_callback(index):
    number = index + 1
    offset = "" 
    if number < 100:
        offset = "00" if number < 10 else "0"
    variables["#num_ticket1"]=f"Nº {offset}{number + 0 + number*5 - 1*index}" 
    variables["#num_ticket2"]=f"Nº {offset}{number + 1 + number*5 - 1*index}"
    variables["#num_ticket3"]=f"Nº {offset}{number + 2 + number*5 - 1*index}"
    variables["#num_ticket4"]=f"Nº {offset}{number + 3 + number*5 - 1*index}"
    variables["#num_ticket5"]=f"Nº {offset}{number + 4 + number*5 - 1*index}"

def main(total_of_files):
    for i in range(total_of_files):
        xmldoc = minidom.parse('./teste.svg')
        create_new_xml(i, xmldoc, custom_callback)

def create_new_xml(index, xmldoc, callback_variables):
    elements = xmldoc.getElementsByTagName('tspan')
    replace_variables(elements)
    with open(f"teste_{index+1}.svg", "w") as file:
        xmldoc.writexml(file)
    callback_variables(index)

def test():
    xmldoc = minidom.parse('./teste.svg')
    elements = xmldoc.getElementsByTagName('tspan')
    replace_variables(elements, {"s": "isso mesmo"})
    with open("teste_1.svg", "w") as file:
        xmldoc.writexml(file)

if __name__ == "__main__":
    main(44)
        
    
