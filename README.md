# Binary Search Tree (BST) — Python

Простой модуль на Python 3.8+ с реализацией бинарного дерева поиска.

Файлы:
- [bst/tree.py](bst/tree.py): реализация `TreeNode` и `BinarySearchTree`.
- [example.py](example.py): пример использования и простая проверка методов.
- [requirements.txt](requirements.txt): зависимости (пусто — стандартная библиотека).

Как запустить

1. Создайте виртуальное окружение (рекомендуется):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Установите зависимости (если есть):

```powershell
pip install -r requirements.txt
```

3. Запустите пример:

```powershell
python example.py
```

Описание API

- `TreeNode` — узел дерева.
- `BinarySearchTree.insert(key, value)` — вставка/обновление пары.
- `BinarySearchTree.search(key)` — возвращает `value` или `None`.
- `BinarySearchTree.delete(key)` — удаляет и возвращает `True`/`False`.
- `BinarySearchTree.height()` — высота (число узлов в максимальном пути, пустое дерево -> 0).
- `BinarySearchTree.is_balanced()` — проверяет баланс (разница высот поддеревьев ≤ 1 для всех узлов).
