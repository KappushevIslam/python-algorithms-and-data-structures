"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTreeError(Exception):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
        while True:
            try:
                if self.left_child is None and new_node < self.root:
                    self.left_child = BinaryTree(new_node)
                elif new_node < self.root:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
                else:
                    raise BinaryTreeError("*** Ошибка! Левый потомок должен быть меньше родителя ***")
            except (ValueError, BinaryTreeError) as err:
                print(err)
                new_node = int(input(f'Введите число меньше {self.root}: '))
            else:
                break

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
        while True:
            try:
                if self.right_child is None and new_node > self.root:
                    self.right_child = BinaryTree(new_node)
                elif new_node > self.root:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    raise BinaryTreeError(" Ошибка, праввый потомок должен быть больше родителя!")
            except (ValueError, BinaryTreeError) as err:
                print(err)
                new_node = int(input(f'Введите число больше {self.root}: '))
            else:
                break

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


my_tree = BinaryTree(10)
my_tree.insert_left(40)
print(my_tree.get_left_child())
print(my_tree.get_left_child().get_root_val())
my_tree.insert_right(12)
my_tree.insert_right(6)
print(my_tree.get_right_child())
print(my_tree.get_right_child().get_root_val())
my_tree.get_right_child().set_root_val(16)
