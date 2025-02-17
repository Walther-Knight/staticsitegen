import unittest

from htmlnode import HTMLNode, LeafNode

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
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
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
            None,
            None
    )
        self.assertEqual(
            node.to_html(), '<p>Test Value!</p>'
    )
        
    def test_children_not_none(self):
        node = LeafNode(
            "p",
            "Test Value!",
            "Children!",
            None
    )
        self.assertEqual(
            node.children, None
    )

    def test_value_required(self):
        LeafNode(
            "p",
            None, {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    )
        self.assertRaises(
            ValueError
    )


if __name__ == "__main__":
    unittest.main()