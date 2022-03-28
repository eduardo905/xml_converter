# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lxml import etree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    inputXml = etree.parse("input.xml")
    outXml = etree.Element("root")
    for knob in inputXml.getiterator("warning"):
        path = knob.get("path").split('/')
        root = outXml
        while path:
            page_name = path.pop(0)
            print(page_name)
            for child in root.iterchildren():
                if child.get('name') == page_name:
                    print("found {}".format(page_name))
                    root = child
                    break
            else:
                new_page = etree.Element("page")
                new_page.set('name', page_name)
                root.append(new_page)
                root = new_page
                print("inserted {}".format(page_name))
        else:
            root.append(knob)
            print(knob.text)

    with open("output.xml", 'w') as file:
        file.write(etree.tostring(outXml, encoding='unicode', pretty_print=True))

    print('bye')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
