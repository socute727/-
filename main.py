import sys

class Stack:
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, number):
        self.sp += 1
        self.buf[self.sp] = number

    def pop(self):
        if self.sp == -1:
            raise Exception("Stack underflow")
        number = self.buf[self.sp]
        self.sp -= 1
        return number

    def top(self):
        if self.sp == -1:
            raise Exception("Stack is empty")
        return self.buf[self.sp]

class Interpreter:
    def __init__(self, program):
        self.program = program
        self.pc = 0
        self.stack = Stack(256)
        self.label_tracker = {}
        self.isinputTrue = False
        self.usinput = None

    def tokenize(self, lines):
        token_counter = 0
        program = []
        for line in lines:
            parts = line.split(" ")
            opcode = parts[0]

            if opcode == "":
                continue

            if opcode.endswith(":"):
                self.label_tracker[opcode[:-1]] = token_counter
                continue

            program.append(opcode)
            token_counter += 1

            if opcode == "гойда":
                number = int(parts[1])
                program.append(number)
                token_counter += 1
            elif opcode == "молвить":
                string_literal = ' '.join(parts[1:])[1:-1]
                program.append(string_literal)
                token_counter += 1
            elif opcode in ["ежели.равно.0", "ежели.больше.0", "ежели.меньше.0", "ежели.равно", "ежели.больше"]:
                label = parts[1]
                program.append(label)
                token_counter += 1
        self.program = program

    def run(self):
        while self.program[self.pc] != "славянский.зажим.яйцами":
            opcode = self.program[self.pc]
            self.pc += 1

            if opcode == "славянский.разжим.яйцами":
                continue

            if opcode == "гойда":
                number = self.program[self.pc]
                self.pc += 1
                self.stack.push(number)
           
            elif opcode == "перун":
                self.stack.pop()
           
            elif opcode == "воздать.сумму":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b + a)
                string = b + a
           
            elif opcode == "воздать.разницу":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b - a)
                string = b - a
           
            elif opcode == "воздать.произведение":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b * a)
                string = b * a
           
            elif opcode == "воздать.частное":
                a = self.stack.pop()
                b = self.stack.pop()
                self.stack.push(b / a)
                string = b / a
           
            elif opcode == "воздать.знак.математический":
                сложение = False
                вычетание = False
                произведение = False
                деление = False
                
                if string == "+":
                    сложение = True
                
                elif string == "-":
                    вычетание = True
                
                elif string == "/":
                    деление = True
                
                elif string == "*":
                    умножение = True
                
                
                else:
                    print("Оштибкаошибочка")
                    exit(1)
           
            elif opcode == "воздать.с.знакомзнакушкой":
                if сложение == True:
                    res = b + a
                    
                elif вычетание == True:
                    res = b - a
               
                elif деление == True:
                    res = b / a

                elif умножение == True:
                    res = b * a

            elif opcode == "результат":
                number = self.stack.push(res)
                print(res)
            
            elif opcode == "воздать":
                a = self.stack.pop()
                b = self.stack.pop()
           
            elif opcode == "молвить":
                string_literal = self.program[self.pc]
                self.pc += 1
                print(string_literal)
           
            elif opcode == "молвить.по.памяти":
                string = self.usinput
                if self.isinputTrue:
                    print(self.usinput)
           
            elif opcode == "запамятовать":
                string = self.usinput
                self.usinput = self.stack.pop()
                self.isinputTrue = True
           
            elif opcode == "цифрацифрушка.принять":
                number = int(input())
                self.stack.push(number)
           
            elif opcode == "строкастроченька.принять":
                string = input()
                self.stack.push(string)
           
            elif opcode == "ежели.равно.0":
                number = self.stack.top()
                if number == 0:
                    self.pc = self.label_tracker[self.program[self.pc]]
                else:
                    self.pc += 1
           
            elif opcode == "ежели.больше.0":
                number = self.stack.top()
                if number > 0:
                    self.pc = self.label_tracker[self.program[self.pc]]
                else:
                    self.pc += 1
           
            elif opcode == "ежели.меньше.0":
                number = self.stack.top()
                if number < 0:
                    self.pc = self.label_tracker[self.program[self.pc]]
                else:
                    self.pc += 1
           
            elif opcode == "ежели.равно":
                a = self.stack.pop()
                b = self.stack.pop()
                if a == b:
                    self.pc = self.label_tracker[self.program[self.pc]]
                else:
                    self.pc += 1
           
            elif opcode == "ежели.больше":
                a = self.stack.pop()
                b = self.stack.pop()
                if a > b:
                    self.pc = self.label_tracker[self.program[self.pc]]
                else:
                    self.pc += 1
            else:
                print("Ошибка в синтаксисе старославянском!")
                exit(1)

def main():
    program_filepath = sys.argv[1]
    with open(program_filepath, "r") as program_file:
        program_lines = [line.strip() for line in program_file.readlines()]

    interpreter = Interpreter(program=[])
    interpreter.tokenize(program_lines)
    interpreter.run()

if __name__ == "__main__":
    main()