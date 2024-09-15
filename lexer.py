class Lexer:
    def __init__(self, content: str) -> None:
        self.content: list[str] = [*content]
        self.__content_lock = self.content.copy()

    def trim_left(self) -> None:
        while len(self.content) > 0 and self.content[0].isspace():
            self.content = self.content[1:]

    def chop(self, n: int) -> list[str]:
        token = self.content[:n]
        self.content = self.content[n:]
        return token

    def chop_while(self, predicate) -> list[str]:
        n = 0
        while n < len(self.content) and predicate(self.content[n]):
            n += 1
        return self.chop(n)

    def __iter__(self):
        self.content = self.__content_lock
        return self

    def __next__(self) -> str:
        self.trim_left()

        if not self.content:
            raise StopIteration

        if self.content[0].isnumeric():
            return "".join(self.chop_while(lambda x: x.isnumeric()))

        if self.content[0].isalpha():
            return "".join(list(map(lambda x: x.upper(),
                                    self.chop_while(lambda x: x.isalnum()))))

        return "".join(self.chop(1))
