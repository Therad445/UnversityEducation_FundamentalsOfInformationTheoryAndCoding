class element:
    def __init__(self, value=-1, right=None, left=None, count=0):
        self.value = value # Значение элемента (-1 если это просто точка (S как принято в презах))
        self.right = right # типо ссылка на правый
        self.left = left # типо ссылка на левый
        self.count = count # количество элементов (частота)
    
    def is_end(self):
        return self.value != -1


# Тут оно парситься из [(элемент, частота), ... ]
def to_list_graph(array):
    list_graph = []

    for elem in array:
        list_graph.append(element(elem[0], None, None, elem[1]))

    return list_graph


# Сортировка по частотам
def graph_list_sort_by_count(array):
    array.sort(key=lambda x: x.count, reverse=True)


# Вот тут оно парсится из листа типа [(левая ветка, правая ветка), ... ]
def to_graph(array):
    if len(array) == 1:
        return array[0]

    graph_list_sort_by_count(array)
    print([a.value for a in array])

    el1 = array[-1]
    el2 = array[-2]

    array[-2] = element(-1, el1, el2, el1.count + el2.count)
    array.pop(-1)
    return to_graph(array)


# Проходится по веткам
def iter_next(data, el, code):
    if el.left.is_end():
        data[el.left.value] = code + '0'
    else:
        iter_next(data, el.left, code + '0')

    if el.right.is_end():
        data[el.right.value] = code + '1'
    else:
        iter_next(data, el.right, code + '1')


def encode_code(graph):
    data = dict()

    iter_next(data, graph, '')

    return data


def main():
    data = [(4, 5), (0, 2), (1, 1), (2, 1), (3, 1), (5, 1), (6, 1), (7, 1)]

    list_graph = to_list_graph(data)

    graph = to_graph(list_graph)

    res = encode_code(graph)

    print(res)

        
main()