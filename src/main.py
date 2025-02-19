from textnode import *
from htmlnode import *
from texthandling import *

def main():
    node = TextNode("**bold** and *italic*", TextType.TEXT)
# First pass - bold
    nodes_after_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
# Second pass - italic
    final_nodes = split_nodes_delimiter(nodes_after_bold, "*", TextType.ITALIC)

    print(nodes_after_bold)
    print(final_nodes)

main()