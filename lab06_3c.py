class PDA:
    def __init__(self):
        self.q0, self.q1, self.q2, self.q3 = 'q0', 'q1', 'q2', 'q3'
        self.state = self.q0
        self.stack = ['Z0']  # Pila inicial con Z0 en el fondo

    def transition(self, symbol):
        if self.state == self.q0:
            if symbol == 'a' and self.stack[-1] == 'Z0':
                self.stack.append('A')
                return True
            elif symbol == 'a' and self.stack[-1] == 'A':
                self.stack.append('A')
                return True
            elif symbol == 'b':
                self.state = self.q1 
                return True
        elif self.state == self.q1:
            if symbol == 'b' and self.stack[-1] == 'A':
                self.stack.append('B')
                return True
            elif symbol == 'c' and self.stack[-1] == 'B':
                self.state = self.q2
                self.stack.pop() 
                return True
        elif self.state == self.q2:
            if symbol == 'c' and self.stack[-1] == 'B':
                self.stack.pop()
                return True
            elif symbol == 'd' and self.stack[-1] == 'A':
                self.state = self.q3
                self.stack.pop()
                return True
        elif self.state == self.q3:
            if symbol == 'd' and self.stack[-1] == 'A':
                self.stack.pop()
                return True
            elif symbol == 'ε' and self.stack[-1] == 'Z0':
                return True 
        return False 

    def accepts(self, input_string):
        self.state = self.q0
        self.stack = ['Z0']

        for symbol in input_string:
            if not self.transition(symbol):
                return False

        return self.transition('ε') and self.state == self.q3

pda = PDA()
examples = ['aabbccdd', 'aaabbbcccddd', 'abccd', 'aabbccdd', 'aaabbccddd']  
for example in examples:
    if pda.accepts(example):
        print(f"La cadena '{example}' es aceptada.")
    else:
        print(f"La cadena '{example}' no es aceptada.")

