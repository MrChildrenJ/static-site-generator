class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value          # no value -> must has children
        self.children = children    # no children -> must has value
        self.props = props          # dictionary of key-value pairs representing the attributes of the HTML tag
    
    def to_html(self):
        raise NotImplementedError("abstract methods should raise this exception when they require derived classes to override the method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        res = []
        for key, val in self.props.items():
            res.append(f' {key}="{val}"')
        return "".join(res)

    def __repr__(self):
        res = []
        res.append(f"tag = {self.tag}")
        res.append(f"value = {self.value}")
        res.append(f"children = {self.children}")
        res.append(f"props = {self.props}")
        return "\n".join(res)
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)   # Leaf must has no children

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        # ex: <a href="https://www.google.com">Click me!</a>
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        res = []
        res.append(f"tag = {self.tag}")
        res.append(f"value = {self.value}")
        res.append(f"props = {self.props}")
        return "\n".join(res)
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"