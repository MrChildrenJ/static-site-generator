import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single(self):
        node = HTMLNode(tag="a", value="click me", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn(' href="https://example.com"', result)
        self.assertIn(' target="_blank"', result)

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="hello")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="hello", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_raises(self):
        node = HTMLNode(tag="div", value="content")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr_contains_all_fields(self):
        node = HTMLNode(tag="span", value="text", children=None, props={"class": "bold"})
        r = repr(node)
        self.assertIn("tag = span", r)
        self.assertIn("value = text", r)
        self.assertIn("children = None", r)
        self.assertIn("props = {'class': 'bold'}", r)

    def test_default_fields_are_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


if __name__ == "__main__":
    unittest.main()
