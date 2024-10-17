class PDA:
    def __init__(self):
        # Estados
        self.q0, self.q1, self.q2 = 'q0', 'q1', 'q2'
        # Configuración inicial
        self.state = self.q0
        self.stack = ['Z0']  # Pila inicial con Z0 en el fondo

    def transition(self, symbol):
        if self.state == self.q0:
            if symbol == '0' and self.stack[-1] == 'Z0':
                self.stack.extend(['X', 'X'])  # Agregar XX en la pila
                return True
            elif symbol == '0' and self.stack[-1] == 'X':
                self.stack.append('X')  # Agregar X en la pila
                return True
            elif symbol == '1' and self.stack[-1] == 'X':
                self.state = self.q1
                self.stack.pop()  # Quitar X de la pila
                return True
        elif self.state == self.q1:
            if symbol == '1' and self.stack[-1] == 'X':
                self.stack.pop()  # Quitar X de la pila
                return True
            elif symbol == 'ε' and self.stack[-1] == 'Z0':
                self.state = self.q2  # Cambio a estado final q2
                return True
        return False  # Transición inválida

    def accepts(self, input_string):
        # Reiniciar el autómata para cada nueva cadena
        self.state = self.q0
        self.stack = ['Z0']

        # Procesar cada símbolo en la cadena de entrada
        for symbol in input_string:
            if not self.transition(symbol):
                return False

        # Procesar transición con ε al final
        return self.transition('ε') and self.state == self.q2

# Ejemplos de uso
pda = PDA()
examples = ['0011', '000111', '011', '0001111']  # Cadenas de prueba
for example in examples:
    if pda.accepts(example):
        print(f"La cadena '{example}' es aceptada.")
    else:
        print(f"La cadena '{example}' no es aceptada.")
