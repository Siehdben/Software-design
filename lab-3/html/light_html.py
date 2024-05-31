class LightNode:
    def render(self):
        raise NotImplementedError

class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text

class LightElementNode(LightNode):
    def __init__(self, tag, css_classes=None):
        self.tag = tag
        self.css_classes = css_classes if css_classes else []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def render(self):
        classes = " ".join(self.css_classes)
        open_tag = f"<{self.tag} class='{classes}'>"
        close_tag = f"</{self.tag}>"
        inner_html = "".join([child.render() for child in self.children])
        return f"{open_tag}{inner_html}{close_tag}"

class FlyweightFactory:
    _instances = {}

    @staticmethod
    def get_instance(tag):
        if tag not in FlyweightFactory._instances:
            FlyweightFactory._instances[tag] = LightElementNode(tag)
        return FlyweightFactory._instances[tag]
