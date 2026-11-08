class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self._size = 0

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            self._size += 1
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current, value):

        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                self._size += 1
            else:
                self._add_recursive(current.left, value)

        else:
            if current.right is None:
                current.right = Node(value)
                self._size += 1
            else:
                self._add_recursive(current.right, value)

    def contains(self, value):

        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._contains_recursive(current.left, value)
        else:
            return self._contains_recursive(current.right, value)

    def find_min(self):

        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):

        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def count(self):

        return self._size

    def get_all_in_order(self):

        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)

    def display(self):

        elements = self.get_all_in_order()
        print(f"Елементи дерева (in-order): {elements}")

    def delete(self, value):

        if not self.contains(value):
            return False
        self.root = self._delete_recursive(self.root, value)
        self._size -= 1
        return True

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:

            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left


            min_node = self._find_min_node(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current



if __name__ == "__main__":
    tree = BinarySearchTree()


    values_to_add = [3, 1, 9, 1, 7, 10, 6, 8]
    print("--- 1. Додавання елементів ---")
    for val in values_to_add:
        tree.add(val)
    print(f"Додано елементи: {values_to_add}")

    print("\n--- 2. Виведення всіх елементів ---")
    tree.display()

    print("\n--- 3. Загальна кількість та крайні значення ---")
    print(f"Кількість елементів в дереві: {tree.count()}")
    print(f"Найменший елемент: {tree.find_min()}")
    print(f"Найбільший елемент: {tree.find_max()}")

    print("\n--- 4. Пошук елементів ---")
    print(f"Чи є елемент 7 у дереві?: {tree.contains(7)}")
    print(f"Чи є елемент 15 у дереві?: {tree.contains(15)}")

    print("\n--- 5. Видалення елемента ---")
    print("Видаляємо елемент 3...")
    tree.delete(3)
    tree.display()
    print(f"Нова кількість елементів: {tree.count()}")
    print(f"Найменший елемент: {tree.find_min()}")
    print(f"Найбільший елемент: {tree.find_max()}")