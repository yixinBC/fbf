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
    def __init__(self) -> None:
        self.value: Any = 0
        self.next: Cell | None = None
        self.prev: Cell | None = None


class DefaultCell(Cell):
    def __init__(self) -> None:
        self.value: int = 0
        self.next: DefaultCell | None = None
        self.prev: DefaultCell | None = None


class u8Cell(Cell):
    def __init__(self) -> None:
        self.value: u8 = u8(0)
        self.next: u8Cell | None = None
        self.prev: u8Cell | None = None


class u16Cell(Cell):
    def __init__(self) -> None:
        self.value: u16 = u16(0)
        self.next: u16Cell | None = None
        self.prev: u16Cell | None = None
