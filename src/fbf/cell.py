"""
this module contains all cell types used in this project
"""


class u8(int):
    """
    u8 value type, used for u8Cell
    """

    def __add__(self, other: int) -> "u8":
        return u8((int(self) + other) % 256)

    def __sub__(self, other: int) -> "u8":
        return u8((int(self) - other) % 256)


class u16(int):
    """
    u16 value type, used for u16Cell
    """

    def __add__(self, other: int) -> "u16":
        return u16((int(self) + other) % 65536)

    def __sub__(self, other: int) -> "u16":
        return u16((int(self) - other) % 65536)


class Cell:
    """
    base Cell type, used for all other cell types
    """

    def __init__(self):
        raise NotImplementedError


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
