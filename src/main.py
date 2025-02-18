from textnode import *
from htmlnode import *

def main():
    text = "This is normal text"
    text_type = TextType.TEXT
    url = {"src": "https://imgur.com/adhdad35f5", "alt": "Alternate Text"}
    
    text_node = TextNode(text, text_type, url)
    
    def test_link_text_node():
        node = TextNode("click here", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        print(html_node)
    # What properties would you expect html_node to have?

    test_link_text_node()

main()