import sys

program_filepath = sys.argv[1]

program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = []
token_counter = 0
label_tracker = {}
for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]

    if opcode == "":
        continue

    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    program.append(opcode)
    token_counter += 1

    if opcode == "пуш":
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    
    elif opcode == "напечатать":
        string_literal = ' '.join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    
    elif opcode in ("если.равно.0", "если.больше.0", "если.меньше.0", "если.равно", "если.больше", "если.меньше"):
        label = parts[1]
        program.append(label)
        token_counter += 1

class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, value):
        self.sp += 1
        self.buf[self.sp] = value
    
    def pop(self):
        value = self.buf[self.sp]
        self.sp -= 1
        return value
    
    def top(self):
        return self.buf[self.sp]

pc = 0
stack = Stack(256)
isinputTrue = False
usinput = None

while program[pc] != "славянский.зажим.яйцами":
    opcode = program[pc]
    pc += 1
    
    if opcode == "гойда":
        value = program[pc]
        pc += 1
        stack.push(value)
    
    elif opcode == "перун":
        stack.pop()     
    
    elif opcode == "воздать.сумму":
        a = stack.pop()
        b = stack.pop()
        stack.push(a + b)
    
    elif opcode == "воздать.разницу":
        a = stack.pop()
        b = stack.pop()
        stack.push(a - b)
    
    elif opcode == "воздать.произведение":
        a = stack.pop()
        b = stack.pop()
        stack.push(a * b)
    
    elif opcode == "воздать.частное":
        a = stack.pop()
        b = stack.pop()
        stack.push(a / b)
    
    elif opcode == "воздать":
        stack.pop()
        stack.pop()
    
    elif opcode == "молвить":
        string_literal = program[pc]
        pc += 1
        print(string_literal)
    
    elif opcode == "молвить.по.памяти":
        if isinputTrue:
            print(usinput)
    
    elif opcode == "запамятовать":
        usinput = stack.pop()
        isinputTrue = True
    
    elif opcode == "цифрациферка":
        value = int(input())
        stack.push(value)
    
    elif opcode == "строкастроченька":
        string = input()
        stack.push(string)
    
    elif opcode == "ежели.равно.0":
        value = stack.top()
        if value == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif opcode == "ежели.больше.0":
        value = stack.top()
        if value > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif opcode == "ежели.меньше.0":
        value = stack.top()
        if value < 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif opcode == "ежели.равно":
        a = stack.pop()
        b = stack.pop()
        if a == b:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif opcode == "ежели.больше":
        a = stack.pop()
        b = stack.pop()
        if a > b:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif opcode == "ежели.меньше":
        a = stack.pop()
        b = stack.pop()
        if a < b:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    
    elif opcode == "перейти":
        label = program[pc]
        pc = label_tracker[label]
    
    else:
        print("Ошибка в синтаксисе стрословянском!")
        exit(1)