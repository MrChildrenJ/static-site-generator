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
    
    