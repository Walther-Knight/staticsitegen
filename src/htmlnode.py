class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode(Tag: {self.tag}, Value: {self.value}, children: {self.children}, Props: {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        if children is not None:
            raise TypeError("LeafNode cannot have children")
        if value == None:
            raise ValueError("Value required for LeafNode")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(Tag: {self.tag}, Value: {self.value}, Props: {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, value, children, props=None):
        if value is not None:
            raise TypeError("ParentNode cannot have HTML value assigned")
        if children == None:
            raise ValueError("ParentNode must have children")
        if tag == None:
            raise ValueError("HTML Tag required for ParentNode")
        super().__init__(tag, None, children, props)

    def to_html(self):
        html_string = ""
        for child in self.children:
                html_string += child.to_html()
        if self.props == None:
            return f"<{self.tag}>{html_string}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode(Tag: {self.tag}, Children: {self.children}, Props: {self.props})"