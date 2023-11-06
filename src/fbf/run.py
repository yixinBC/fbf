"""
module that run a brainfuck source code
"""
from typing import TextIO
from .cell import u8Cell, u16Cell, InfCell


def run_bf_u8(file: TextIO):
    """
    run brainfuck code with u8 cell
    """
    origin_cell = u8Cell()
    current_cell = origin_cell
    loop_stack = []
    while opcode := file.read(1):
        match opcode:
            case ">":  # ++ptr
                if current_cell.next is not None:
                    current_cell = current_cell.next
                else:
                    current_cell.next = u8Cell()
                    current_cell = current_cell.next
            case "<":  # --ptr
                if current_cell.prev is not None:
                    current_cell = current_cell.prev
                else:
                    current_cell.prev = u8Cell()
                    current_cell = current_cell.prev
            case "+":  # ++*ptr
                current_cell.value += 1
            case "-":  # --*ptr
                current_cell.value -= 1
            case ".":  # putchar(*ptr)
                print(bytes((current_cell.value,)), end="")
            case ",":  # *ptr = getchar()
                pass
            case "[":  # while (*ptr) {
                if current_cell.value:
                    if file.tell() not in loop_stack:
                        loop_stack.append(file.tell())
                else:
                    file.seek(loop_stack.pop())
            case "]":  # }
                file.seek(loop_stack[-1])
            case _:
                raise ValueError(f"Invalid opcode: {opcode}")


def run_bf_u16(file: TextIO):
    """
    run brainfuck code with u16 cell
    """
    origin_cell = u16Cell()
    current_cell = origin_cell
    loop_stack = []
    while opcode := file.read(1):
        match opcode:
            case ">":  # ++ptr
                if current_cell.next is not None:
                    current_cell = current_cell.next
                else:
                    current_cell.next = u16Cell()
                    current_cell = current_cell.next
            case "<":  # --ptr
                if current_cell.prev is not None:
                    current_cell = current_cell.prev
                else:
                    current_cell.prev = u16Cell()
                    current_cell = current_cell.prev
            case "+":  # ++*ptr
                current_cell.value += 1
            case "-":  # --*ptr
                current_cell.value -= 1
            case ".":  # putchar(*ptr)
                print(bytes((current_cell.value,)), end="")
            case ",":  # *ptr = getchar()
                pass
            case "[":  # while (*ptr) {
                if current_cell.value:
                    if file.tell() not in loop_stack:
                        loop_stack.append(file.tell())
                else:
                    file.seek(loop_stack.pop())
            case "]":  # }
                file.seek(loop_stack[-1])
            case _:
                raise ValueError(f"Invalid opcode: {opcode}")


def run_bf_inf(file: TextIO):
    """
    run brainfuck code with inf cell
    """
    origin_cell = InfCell()
    current_cell = origin_cell
    loop_stack = []
    while opcode := file.read(1):
        match opcode:
            case ">":  # ++ptr
                if current_cell.next is not None:
                    current_cell = current_cell.next
                else:
                    current_cell.next = InfCell()
                    current_cell = current_cell.next
            case "<":  # --ptr
                if current_cell.prev is not None:
                    current_cell = current_cell.prev
                else:
                    current_cell.prev = InfCell()
                    current_cell = current_cell.prev
            case "+":  # ++*ptr
                current_cell.value += 1
            case "-":  # --*ptr
                current_cell.value -= 1
            case ".":  # putchar(*ptr)
                print(bytes((current_cell.value,)), end="")
            case ",":  # *ptr = getchar()
                pass
            case "[":  # while (*ptr) {
                if current_cell.value:
                    if file.tell() not in loop_stack:
                        loop_stack.append(file.tell())
                else:
                    file.seek(loop_stack.pop())
            case "]":  # }
                file.seek(loop_stack[-1])
            case _:
                raise ValueError(f"Invalid opcode: {opcode}")


def run_bf(file: TextIO, mode: str):
    """
    Delegate function, select and call the appropriate backend function for execution
    """
    match mode:
        case "u8":
            run_bf_u8(file)
        case "u16":
            run_bf_u16(file)
        case "inf":
            run_bf_inf(file)
        case _:
            raise ValueError(f"Invalid mode: {mode}")
