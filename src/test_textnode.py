import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_all_type(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        node3 = TextNode("This is an italic node", TextType.ITALIC)
        node4 = TextNode("This is a code node", TextType.CODE)
        node5 = TextNode("This is a links node", TextType.LINKS)
        node6 = TextNode("This is an images node", TextType.IMAGES)
        #test not equivalent
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)
    
    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.LINKS)
        node2 = TextNode("This is a text node", TextType.LINKS)
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



if __name__ == "__main__":
    unittest.main()