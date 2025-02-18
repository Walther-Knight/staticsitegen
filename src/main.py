from textnode import *
from htmlnode import *

def main():
    node = ParentNode(
                "p",
                None,
                [
                    ParentNode("PARENT",
                    None,
                    [
                        LeafNode(None, "Normal text")
                    ],
                    None
                )
            ],
            None
        )


    print(node.to_html())

main()