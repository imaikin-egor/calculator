class Calculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}

    def tokenize_expression(self, expression):
        tokens = []
        num = ''
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    tokens.append(num)
                    num = ''
                if char in self.operators or char in '()':
                    tokens.append(char)
        if num:
            tokens.append(num)
        return tokens

    def shunting_yard_algorithm(self, tokens):
        output = []
        stack = []
        for token in tokens:
            if token.isdigit() or '.' in token:
                output.append(token)
            elif token in self.operators:
                while (stack and stack[-1] in self.operators and
                       self.operators[stack[-1]] >= self.operators[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
        while stack:
            output.append(stack.pop())
        return output

    def calculate_rpn(self, rpn_expression):
        stack = []
        for token in rpn_expression:
            if token.isdigit() or '.' in token:
                stack.append(float(token))
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError('Invalid expression')
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ValueError('Division by zero')
                    stack.append(a / b)
        if len(stack) != 1:
            raise ValueError('Invalid expression')
        return stack[0]
