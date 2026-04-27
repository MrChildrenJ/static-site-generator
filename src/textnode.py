from enum import Enum

class TextType(Enum):
    PLAIN = "plain_text"
    BOLD = "bold_text"
    ITALIC = "italic_text"
    CODE = "code_text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, type: TextType, url=None):
        self.text = text
        self.text_type = type
        self.url = url
    
    def __eq__(self, other: TextNode):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"