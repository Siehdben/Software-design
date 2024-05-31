from light_html import LightTextNode, FlyweightFactory


def main():
    filename = "book.txt"  # Змінено на правильний шлях

    # Зчитуємо вміст файлу з вказанням кодування UTF-8
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()

    document = []

    for i, line in enumerate(content):
        line = line.rstrip()  # Видаляємо зайві пробіли справа
        if i == 0:
            node = FlyweightFactory.get_instance("h1")
        elif len(line) < 20:
            node = FlyweightFactory.get_instance("h2")
        elif line.startswith(" "):
            node = FlyweightFactory.get_instance("blockquote")
        else:
            node = FlyweightFactory.get_instance("p")

        text_node = LightTextNode(line)
        node.add_child(text_node)
        document.append(node)

    for element in document:
        print(element.render())


if __name__ == "__main__":
    main()
