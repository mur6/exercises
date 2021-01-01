from pathlib import Path
import sys

# > ++ptr;
# < --ptr;
# + ++(*ptr);
# - --(*ptr);
# . putchar(*ptr);
# , *ptr = getchar();
# [ while(*ptr) {
# ] }
class InputReader:
    def __init__(self):
        self.input_buffer = []
        self.index = 0

    def _one_char(self):
        return self.input_buffer[self.index]

    def read_one_char(self):
        if not self.input_buffer:
            self.input_buffer = list(input(""))
            self.index = 0
            return self.

def bf(program):
    memory_size = 2000
    buffer = [0] * memory_size

    ptr = 0
    counter = 0
    while True:
        inst = program[counter]
        if inst == ">":
            ptr += 1
            if memory_size <= ptr:
                raise ValueError("Invalid program")
        elif inst == "<":
            ptr -= 1
            if ptr < 0:
                raise ValueError("Invalid program")
        elif inst == "+":
            buffer[ptr] += 1
        elif inst == "-":
            buffer[ptr] -= 1
        elif inst == ".":
            c = chr(buffer[ptr])
            print(c, end="")
        elif inst == ",":
            one_char = read_one_char()
            buffer[ptr] = ord(one_char)
        elif inst == "[": # while(*ptr) {
            if buffer[ptr] == 0:
                while program[counter] != "]":
                    counter += 1
        elif inst == "]": # end of while loop.
            while program[counter] != "[":
                counter -= 1
            continue
        else:
            break
        counter += 1

if __name__ == '__main__':
    bf(Path(sys.argv[1]).read_text())
