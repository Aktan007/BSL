from bst import BinarySearchTree


def main():
    bst = BinarySearchTree()
    data = [(50, 'a'), (30, 'b'), (70, 'c'), (20, 'd'), (40, 'e'), (60, 'f'), (80, 'g')]
    for k, v in data:
        bst.insert(k, v)

    print('Inorder items:', list(bst.inorder_items()))
    print('Search 40: ', bst.search(40))
    print('Height: ', bst.height())
    print('Is balanced: ', bst.is_balanced())

    print('Delete 70: ', bst.delete(70))
    print('Inorder after delete:', list(bst.inorder_items()))
    print('Height after delete: ', bst.height())
    print('Is balanced after delete: ', bst.is_balanced())

if __name__ == '__main__':
    main()
