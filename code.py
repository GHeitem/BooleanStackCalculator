import operator
class customExc(Exception):
    pass

ops = {
    '&': {'priority': 1, 'action': operator.and_},
    '|': {'priority': 0, 'action': operator.or_},
    '!': {'priority': 3, 'action': operator.not_},
    '(': {'priority': 4},
    ')': {'priority': 1},
}
operands = [chr(x) for x in range(ord('a'), ord('z') + 1)] + ['0', '1']
variables = [chr(x) for x in range(ord('a'), ord('z') + 1)]


def a_prior_b(a, b):
    return ops[a]['priority'] >= ops[b]['priority']


def check_expression(exp):
    stack = []
    rpn = []
    for char in exp:
        if char in operands:
            rpn.append(char)
        elif char in ops:
            if char == ')':
                tmp = stack.pop()
                while stack and tmp != '(':
                    rpn.append(tmp)
                    tmp = stack.pop()
            if not stack:
                stack.append(char)
            else:
                while stack and a_prior_b(stack[len(stack) - 1], char) \
                        and stack[len(stack) - 1] != '(':
                    rpn.append(stack.pop())
                if char != ')':
                    stack.append(char)
        else:
            raise customExc("Ошибка. Неверные символы в строке")
    for x in reversed(stack):
        rpn.append(x)
    tmp = "".join(rpn)
    return tmp


def get_lookup_table(vect):
    i = 0
    lookup = {}
    while i < len(vect):
        lookup[variables[i]] = vect[i]
        i = i + 1
    return lookup


def evaluate(expression, lookup):
    result = ""
    for x in expression:
        if x in lookup.keys():
            result = result + str(lookup[x])
            print(result)
        else:
            result = result + expression[expression.index(x)]
            print(result)
    return result
def calculate(evaluated):
    stack=[]
    for x in evaluated:
        if x in {'0','1'}:
            stack.append(x)
           # print(stack);
        elif x in ops:
            try:
                op1 = int(stack.pop())
                if x != '!':
                    op2 = int(stack.pop())
                    stack.append(str(ops[x]['action'](op1,op2)))
               #     print(stack)
                else:
                    stack.append(str(~op1))
                #    print(stack)
            except: IndexError("Ошибка. Несовпадение значений и операторов")
        else:
            raise customExc("Ошибка. Формула содержит недопустимые символы или подставлены не все значения")
    print(stack)
    if len(stack) != 1:
        raise customExc("Ошибка. Формула не является допустимой обратной записью")
    else:
        return stack == ['1']


if __name__ == '__main__':
    s = "a&(b|(c&!d))"
    print("Исходная строка: ",s)
    invS=check_expression(s)
    print("Обратная запись: ",invS)
    vect = [0, 0, 1, 0]
    tmp = get_lookup_table(vect)
    print("Подстановочный словарь:", tmp)
    evalExp = evaluate(invS, tmp)
    print("Evaluate: ", evalExp)
    print("Результат: ", calculate(evalExp))
