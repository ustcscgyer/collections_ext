def infixToPostfix(s):
    postfix, op = [], []
    oprants = '+-*/'
    prec = {'*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1}
    for c in s:
        if c == '(':
            op.append(c)
        elif c == ')':
            topToken = op.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = op.pop()
        elif c not in oprants:
            postfix.append(c)
        else:
            while len(op) > 0 and prec[op[-1]] >= prec[c]:
                postfix.append(op.pop())
            op.append(c)
        
    while len(op) > 0:
        postfix.append(op.pop())
        
    return postfix

def evalPostfix(s):
    oprants = '+-*/()'
    prec = {'*' : 3, '/' : 3, '+' : 2, '-' : 2}
    nums = []
    
    for c in s:
        if c not in oprants:
            nums.append(c)
        else:
            n2, n1 = nums.pop(), nums.pop()
            nums.append(eval(str(n1)+c+str(n2)))
            
    assert len(nums) == 1
    return nums[0]

def getTokens(s):
    i, token = 0, []
    while i < len(s):
        if s[i] == ' ':
            if token == []:
                pass
            else:
                yield ''.join(token)
                token = []
        elif s[i] in '+-/*()':
            if token == []:
                yield s[i]
            else:
                yield ''.join(token)
                token = []
                i -= 1
        else:
            token.append(s[i])
        i += 1
            
    if token != []
        yield ''.join(token)
