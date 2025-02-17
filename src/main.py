from textnode import *
from htmlnode import *

def main():
    props = {
    "href": "https://www.google.com",
    "target": "_blank",
}
    tag = "p"
    value = "Test Value!"
    testobj = LeafNode(tag, value, props)
    print(testobj.to_html())

main()