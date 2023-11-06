"""
this module contains all cell types used in this project
"""
from typing import Any


class u8(int):
    """
    u8 value type, used for u8Cell
    """

    def __add__(self, other: int) -> "u8":
        return u8((self + other) % 256)

    def __sub__(self, other: int) -> "u8":
        return u8((self - other) % 256)


class u16(int):
    """
    u16 value type, used for u16Cell
    """

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
        super().__init__()
        self.value: int = value


class u8Cell(Cell):
    """
    Cell that use u8(byte) type as value type, many brainfuck implementation uses this type
    """

    def __init__(self, value=0) -> None:
        super().__init__()
        self.value: u8 = u8(value % 256)


class u16Cell(Cell):
    """
    Cell that use u16(word) type as value type, some brainfuck implementation uses this type
    """

    def __init__(self, value=0) -> None:
        super().__init__()
        self.value: u16 = u16(value % 65536)
