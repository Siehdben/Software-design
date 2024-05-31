from light_element_node import LightElementNode
from light_element_node import LightTextNode

def main():
    div = LightElementNode("div", "block", "double", ["container"])
    p = LightElementNode("p", "block", "double", ["paragraph"])
    text = LightTextNode("This is a sample text.")
    p.add_child(text)
    div.add_child(p)

    print(div.render())

if __name__ == "__main__":
    main()
