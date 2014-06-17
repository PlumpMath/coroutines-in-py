import xml.parsers.expat

def expat_parse(f,target):
    parser = xml.parsers.expat.ParserCreate()
    parser.buffer_size = 65536
    parser.buffer_text = True
    parser.returns_unicode = False
    parser.StartElementHandler = \
       lambda name,attrs: target.send(('start',(name,attrs)))
    parser.EndElementHandler = \
       lambda name: target.send(('end',name))
    parser.CharacterDataHandler = \
       lambda data: target.send(('text',data))
    parser.ParseFile(f)

# Example.  This uses the bus processing code from earlier with no changes.

if __name__ == '__main__':
    from buses import *

    expat_parse(open("allroutes.xml"),
            buses_to_dicts(
            filter_on_field("route","22",
            filter_on_field("direction","North Bound",
            bus_locations()))))
