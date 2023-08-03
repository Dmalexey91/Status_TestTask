items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
        ]


class TreeStore():
    initialtree = []    #Просто определяем свойство, в котором хранятся исходные данные. Сохраним их для быстрого отображения в будущем
    tree = {}           #Сюда будет писаться дозаполненное дерево для быстрой работы поиска и прямым обращениям по id

    def __init__(self, items):
        self.initialtree = []                                   #Заполняем дерево при инициализации класса

        for leaf in items:                                      #Это необходимо для дальнейшего обращения по id элемента без поиска в цикле
            self.initialtree.append(dict(leaf))                 #Копируем текущий список словарей без ссылок
            self.tree[leaf['id']] = leaf

            if 'parents' not in leaf: leaf['parents'] = []      # Определяем список, в котором будут храниться родители.    Да и в будущем проще обращаться не проверяя на наличие свойства
            if 'children' not in leaf: leaf['children'] = []    # Определяем список, в котором будут храниться дети.        Да и в будущем проще обращаться не проверяя на наличие свойства

            # 1. Рассчитаем всех родителей для каждого элемента
            if leaf['parent'] != 'root':                        #Отталкиваемся от того, что здесь в будущем ожидается только число. В противном случае добавляем проверку на тип и заполненность
                parent = self.initialtree[leaf['parent'] - 1]
                leaf['parents'].append(parent)

                ParentLeaf = items[leaf['parent'] - 1]
                Parentslist = ParentLeaf['parents']
                for element in Parentslist:
                    if element not in leaf['parents']:
                        leaf['parents'].append(element)         #Добавляем родителей из родителей. Так же можно это завернуть в отдельную рекурсивную функцию

                # 2. И тут же записываем текущий элемент как дочку для родителя
                ChildrenLeaf = ParentLeaf['children']
                CurrenLeaf = self.initialtree[leaf['id']-1]
                if CurrenLeaf not in ChildrenLeaf:
                    ChildrenLeaf.append(CurrenLeaf)

        return

    def getAll(self):#  - getAll() Должен возвращать изначальный массив элементов.
        return self.initialtree #Возвращаем изначальный массив элементов :)

    def getitem(self, id):#  - getItem(id) Принимает id элемента и возвращает сам объект элемента;
        try: #Просто защита от дурака. Можно так же проверить на вхождение id между 0 и len(self.tree)
            leaf = self.tree[id]
        except:
            print(f'Элемент с ID = {id} отсутствует в дереве')
            leaf = None
        return leaf

    def getChildren(self, id):#  - getChildren(id) Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
        try:  # Просто защита от дурака. Можно так же проверить на вхождение id между 0 и len(self.tree)
            leaf = self.tree[id]
            parents = leaf['children']
        except:
            print(f'Элемент с ID = {id} отсутствует в дереве')
            parents = None
        return parents

    def getAllParents(self, id):
        try: #Просто защита от дурака. Можно так же проверить на вхождение id между 0 и len(self.tree)
            leaf = self.tree[id]
            parents = leaf['parents']
        except:
            print(f'Элемент с ID = {id} отсутствует в дереве')
            parents = None
        return parents

##### основной исполняемый код #####

id = 2

ts = TreeStore(items)
print('Результат выполнения метода getAll():')
print(ts.getAll(),'\n')

print('Результат выполнения метода getitem():')
print(ts.getitem(id),'\n')

print('Результат выполнения метода getChildren():')
print(ts.getChildren(id),'\n')

print('Результат выполнения метода getAllParents():')
print(ts.getAllParents(id),'\n')




