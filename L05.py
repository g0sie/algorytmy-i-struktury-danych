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
        return f"[{self.key}; {self.left}; {self.right}]"
