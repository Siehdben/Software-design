from light_node import LightNode

class LightElementNode(LightNode):
    def __init__(self, tag, display_type, closing_type, css_classes=None):
        super().__init__()
        self.tag = tag
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes if css_classes else []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        classes = " ".join(self.css_classes)
        open_tag = f"<{self.tag} class='{classes}'>"
        close_tag = f"</{self.tag}>" if self.closing_type != "single" else ""
        inner_html = "".join([child.render() for child in self.children])
        return f"{open_tag}{inner_html}{close_tag}"

class LightTextNode(LightNode):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def render(self):
        return self.text
