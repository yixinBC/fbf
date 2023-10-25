from typing import Any


class u8(int):
    def __add__(self, other: int) -> "u8":
        return u8((self + other) % 256)

    def __sub__(self, other: int) -> "u8":
        return u8((self - other) % 256)


class u16(int):
    def __add__(self, other: int) -> "u16":
        return u16((self + other) % 65536)

    def __sub__(self, other: int) -> "u16":
        return u16((self - other) % 65536)


class Cell:
    """
    base Cell type, used for all other cell types
    """

    def __init__(self, value=0) -> None:
        self.value: Any = value
        self.next: Cell | None = None
        self.prev: Cell | None = None


class InfCell(Cell):
    """
    Cell that use python's int type as value type.
    Theoretical Implementation of Brainfuck Primitive Language Specification(maybe)
    """

    def __init__(self, value=0) -> None:
        self.value: int = value
        self.next: InfCell | None = None
        self.prev: InfCell | None = None


class u8Cell(Cell):
    """
    Cell that use u8(byte) type as value type, many brainfuck implementation uses this type
    """

    def __init__(self, value=0) -> None:
        self.value: u8 = u8(value % 256)
        self.next: u8Cell | None = None
        self.prev: u8Cell | None = None


class u16Cell(Cell):
    """
    Cell that use u16(word) type as value type, some brainfuck implementation uses this type
    """

    def __init__(self, value=0) -> None:
        self.value: u16 = u16(value % 65536)
        self.next: u16Cell | None = None
        self.prev: u16Cell | None = None
