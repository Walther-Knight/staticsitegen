from textnode import *
from htmlnode import *

def main():
    text = "Link text [link](https://google.com)."
    text_type = TextType.IMAGE
    url = {"href": "https://google.com"}
    
    text_node = TextNode(text, text_type, url)
    #output = (text_node_to_html_node(text_node))
    #print(output.tag)
    #print(output.to_html())

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        text_list = old_nodes.text.split(" ")
        print(text_list)
        new_nodes = []
        delimit_start = None
        delimit_end = None
        if delimiter == "[link]":
            for word in range(len(text_list)):
                if text_list[word].startswith(delimiter):
                    delimit_start = word
            new_nodes.append(TextNode(" ".join(text_list[0:delimit_start]), TextType.TEXT, None))
            new_nodes.append(TextNode(" ".join(text_list[delimit_start:delimit_start + 1]).replace(delimiter, "").replace("(", "").replace(")", ""), text_type, url))
            if text_list[delimit_start + 1:]:
                new_nodes.append(TextNode(" ".join(text_list[delimit_start + 1:]), TextType.TEXT, None))
            return new_nodes
        if delimiter == "!":
            print("STUFF")
            return "STUFF"
        
        for word in range(len(text_list)):
            if text_list[word].startswith(delimiter):
                delimit_start = word
            if text_list[word].endswith(delimiter):
                delimit_end = word + 1
        if delimit_start is not None:
            new_nodes.append(TextNode(" ".join(text_list[0:delimit_start]), TextType.TEXT, None))
            new_nodes.append(TextNode(" ".join(text_list[delimit_start:delimit_end]).replace(delimiter, ""), text_type, None))
            if text_list[delimit_end:]:
                new_nodes.append(TextNode(" ".join(text_list[delimit_end:]), TextType.TEXT, None))
            return new_nodes
        return old_nodes





    output = split_nodes_delimiter(text_node, "[link]", TextType.LINK)
    #print(text_node_to_html_node(output).to_html())
    for each in output:
        print(text_node_to_html_node(each).to_html())

main()