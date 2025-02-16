from textnode import *
from htmlnode import *

def main():
    props = {
    "href": "https://www.google.com",
    "target": "_blank",
}
    testobj = HTMLNode(None,None,None,props)
    print(testobj.props_to_html())
    print(props)

main()