"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
string = input("Пожалуйста введите строку которую хотите зашифровать: ")


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman_tree(node, left=True, bin_string=''):
    if type(node) is str:
        return {node: bin_string}
    (left, right) = node.children()
    my_dict = dict()
    my_dict.update(huffman_tree(l, True, bin_string + '0'))
    my_dict.update(huffman_tree(r, False, bin_string + '1'))
    return my_dict


freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, v1) = nodes[-1]
    (key2, v2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, v1 + v2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_tree(nodes[0][0])
print(f'Закодированная строка: {"".join(huffmanCode[char] for char in huffmanCode)}')
