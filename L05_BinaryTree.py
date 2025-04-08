class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert_left(self, key):
        new_left = BinaryTree(key)

        if self.left is None:
            self.left = new_left
        else:
            new_left.left = self.left
            self.left = new_left

    def insert_right(self, key):
        new_right = BinaryTree(key)

        if self.right is None:
            self.right = new_right
        else:
            new_right.right = self.right
            self.right = new_right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_value(self, value):
        self.key = value

    def get_value(self):
        return self.key

    def __str__(self):
        return self._str_helper()

    def _str_helper(self, prefix="", is_left=True):
        result = prefix
        result += "├── " if is_left else "└── "
        result += str(self.key) + "\n"

        if self.left:
            result += self.left._str_helper(
                prefix + ("│   " if is_left else "    "), True
            )

        if self.right:
            result += self.right._str_helper(
                prefix + ("│   " if is_left else "    "), False
            )

        return result

    def insert_node_simple(self, value):
        queue = [self]
        while queue:
            node = queue.pop(0)

            # jeżeli lewy liść jest pusty, to wrzucamy na lewy i kończymy
            if not node.left:
                node.insert_left(value)
                return

            # jak lewy zajęty to wrzucamy lewy do kolejki i lecimy zająć się prawym
            else:
                queue.append(node.left)

            # jeżeli prawy wolny to wrzucamy na prawy i kończymy
            if not node.right:
                node.insert_right(value)
                return

            # jak prawy zajęty to wrzucamy na prawy i lecimy zająć się kolejką
            else:
                queue.append(node.right)
