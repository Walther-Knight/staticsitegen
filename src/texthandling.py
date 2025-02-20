from htmlnode import *
from textnode import *    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        print(node)
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
    #continue loop as long as there is text remaining
        while True:
            delimit_start = text.find(delimiter)
            if delimit_start == -1:
                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                break

            delimit_end = text.find(delimiter, delimit_start + len(delimiter))
            
            if delimit_end == -1:
                raise Exception("Missing closing delimiter in markdown")
            
            if delimit_end != -1:
                if delimit_start > 0:
                    new_nodes.append(TextNode(text[:delimit_start], TextType.TEXT))
                new_nodes.append(TextNode(text[delimit_start + len(delimiter): delimit_end], text_type))
                text = text[delimit_end + len(delimiter):]
            
            
    return new_nodes