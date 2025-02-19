from textnode import *
from htmlnode import *

def main():
    text = "This is **bold** text."
    text_type = TextType.TEXT
    url = {"href": "https://google.com"}
    
    text_node = [TextNode("This is *italic* text.", TextType.TEXT), TextNode("Very *italic*, much text, wow.", TextType.TEXT)]
    text_node1 = TextNode(text, text_type, url)
    old_nodes = [text_node, text_node1]
    #output = (text_node_to_html_node(text_node))
    #print(output.tag)
    #print(output.to_html())

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            delimit_start = node.text.find(delimiter)
            if node.text_type is not TextType.TEXT:
                new_nodes.append(node)
            elif delimit_start != -1:
                delimit_end = node.text.find(delimiter, delimit_start + 1)
                if delimit_end != -1:
                    new_nodes.append(TextNode(node.text[0:delimit_start], TextType.TEXT))
                    new_nodes.append(TextNode(node.text[delimit_start + len(delimiter): delimit_end], text_type))
                    new_nodes.append(TextNode(node.text[delimit_end + len(delimiter) :], TextType.TEXT))
                else:
                    raise Exception("Missing closing delimiter in markdown")
            else:
                new_nodes.append(node)
        return new_nodes





    output = split_nodes_delimiter(text_node, "*", TextType.ITALIC)
    html_out = ""
    for each in output:
        html_out += text_node_to_html_node(each).to_html()
    print(html_out)

main()