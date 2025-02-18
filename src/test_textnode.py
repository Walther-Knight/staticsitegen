import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
#test cases for TextNode base function
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_all_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        node3 = TextNode("This is an italic node", TextType.ITALIC)
        node4 = TextNode("This is a code node", TextType.CODE)
        node5 = TextNode("This is a links node", TextType.LINK)
        node6 = TextNode("This is an images node", TextType.IMAGE)
        #test not equivalent
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)
    
    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)

    def test_non_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        node3 = TextNode("This is an italic node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node3, node4)
    
    def test_url_populated(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev/")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, None)

#Tests for TextNode to HTMLNode conversion
    def test_normal_text(self):
        text = "This is normal text"
        text_type = TextType.TEXT
        url = None
    
        text_node = TextNode(text, text_type, url)
    
        self.assertEqual(
            str(text_node_to_html_node(text_node)), 'LeafNode(Tag: None, Value: This is normal text, Props: None)'
        )

    def test_bold_text(self):
        text = "This is bold text"
        text_type = TextType.BOLD
        url = None
    
        text_node = TextNode(text, text_type, url)
    
        self.assertEqual(
            str(text_node_to_html_node(text_node)), 'LeafNode(Tag: b, Value: This is bold text, Props: None)'
        )

    def test_italic_text(self):
        text = "This is italic text"
        text_type = TextType.ITALIC
        url = None
    
        text_node = TextNode(text, text_type, url)
    
        self.assertEqual(
            str(text_node_to_html_node(text_node)), 'LeafNode(Tag: i, Value: This is italic text, Props: None)'
        )

    def test_code_block(self):
        text = "This is a code block"
        text_type = TextType.CODE
        url = None
    
        text_node = TextNode(text, text_type, url)
    
        self.assertEqual(
            str(text_node_to_html_node(text_node)), 'LeafNode(Tag: code, Value: This is a code block, Props: None)'
        )

    def test_link(self):
        text = "This is a link"
        text_type = TextType.LINK
        url = "https://imgur.com/adhdad35f5"
    
        text_node = TextNode(text, text_type, url)
    
        self.assertEqual(
            str(text_node_to_html_node(text_node)), "LeafNode(Tag: a, Value: This is a link, Props: {'href': 'https://imgur.com/adhdad35f5'})"
        )

    def test_image(self):
        text = "Alternate Text"
        text_type = TextType.IMAGE
        url = "https://imgur.com/adhdad35f5"
    
        text_node = TextNode(text, text_type, url)
    
        self.assertEqual(
            str(text_node_to_html_node(text_node)), "LeafNode(Tag: img, Value: , Props: {'src': 'https://imgur.com/adhdad35f5', 'alt': 'Alternate Text'})"
        )

if __name__ == "__main__":
    unittest.main()