import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
#HTMLNode test cases
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(Tag: p, Value: What a strange world, children: None, Props: {'class': 'primary'})",
        )
#LeafNode test cases
    def test_props_value(self):
        node = LeafNode(
            "a",
            "Test Value!",
            None,
            {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    )
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com" target="_blank">Test Value!</a>'
    )
        
    def test_tag_with_value(self):
        node = LeafNode(
            "p",
            "Test Value!",
            None
    )
        self.assertEqual(
            node.to_html(), '<p>Test Value!</p>'
    )
        
    def test_children_not_none(self):
        with self.assertRaises(TypeError):
            LeafNode(
            "p",
            "Test Value!",
            "Children!",
            None
    )

    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode(
                "p",
                None,
                None,
                {
                    "href": "https://www.google.com",
                    "target": "_blank"
                }
            )
#ParentNode test cases
    def test_html_out(self):
        node = ParentNode(
            "p",
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            None
        )

    
        self.assertEqual(
            node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_nested_parent(self):
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
            self.assertEqual(node.to_html(), '<p><PARENT>Normal text</PARENT></p>')

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(
                None,
                None,
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
                None
        )
    def test_no_value(self):
        with self.assertRaises(ValueError):
            ParentNode(
                "p",
                None,
                None,
                None
        )

    def test_html_out_with_props(self):
        node = ParentNode(
            "p",
            None,
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {
        "href": "https://www.google.com",
        "target": "_blank",
    }
        )
        self.assertEqual(
            node.to_html(), '<p href="https://www.google.com" target="_blank"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

if __name__ == "__main__":
    unittest.main()