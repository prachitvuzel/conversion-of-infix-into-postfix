#conversion of infix into postfix expression



def convert(infix):
    tokens = list(infix)
    stack = []
    result = []
    operators = {
        "(": 0,

        "-": 1,
        "+": 2,
        "*": 3,
        "/": 4,
        "^": 5,
        "$": 6
    }
    for token in tokens:
        if token == "(":
            stack.append(token)
        elif token not in operators and token != ')':
            result.append(token)
        else:
            if len(stack) == 0:
                stack.append(token)
            elif token != ')':
                if operators[token] > operators[stack[-1]]:
                    stack.append(token)
                else:
                    element = stack.pop()
                    stack.append(token)
                    result.append(element)
        if token == ')':

            while stack[-1] != "(":
                element = stack.pop()
                result.append(element)
            stack.pop()

    stack.reverse()

    return ''.join(result)+''.join(stack)


inp = input("Enter your expression")

result = convert(inp)
print(result)
