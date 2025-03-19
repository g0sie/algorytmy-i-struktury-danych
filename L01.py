class Stack:

    def __init__(self) -> None:
        self.items: list = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> None:
        return self.items.pop()

    def peek(self) -> None:
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


brackets = {"(": ")", "[": "]", "{": "}"}


def is_valid(string: str) -> bool:
    stack = Stack()
    for char in string:
        if char in brackets:
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty():
                return False

            if char != brackets[stack.pop()]:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    print(is_valid("(()()())") == True)
    print(is_valid("((((()))))") == True)
    print(is_valid("(()(((())()))") == False)
    print(is_valid("(())(()))") == False)

    print(is_valid("([]{}())") == True)
    print(is_valid("{([])[({()})}") == False)
    print(is_valid("(({}[{()}])]]") == False)
    print(is_valid("({}({([])()})") == False)

    print(is_valid("(]") == False)
