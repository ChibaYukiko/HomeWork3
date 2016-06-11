# python calculator.py

def readNumber(line, index): # read number
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index): # read +
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index): # read -
    token = {'type': 'MINUS'}
    return token, index + 1

def readMulti(line, index): # read *
    token = {'type': 'Multi'}
    return token, index + 1

def readDivision(line, index): # read /
    token = {'type': 'Divis'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMulti(line, index)
        elif line[index] == '/':
            (token, index) = readDivision(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def md_evaluate(tokens): # * / calculate
    tokens2 = []
    index = 0

    while index < len(tokens):
        number = 0.0
        if tokens[index]['type'] == 'NUMBER':
            
            if tokens[index+1]['type'] == 'Multi':
                number = tokens[index]['number']*tokens[index+2]['number']
                token = {'type': 'NUMBER', 'number': number}
                index += 3
                
            elif tokens[index+1]['type'] == 'Divis':
                number = tokens[index]['number']*1.0/tokens[index+2]['number']
                token = {'type': 'NUMBER', 'number': number}
                index += 3
                
            elif tokens[index+1]['type'] in {'PLUS','MINUS'} :
                token = {'type': 'NUMBER', 'number': tokens[index]['number']}
                index += 1
            else:
                print 'Invalid syntax'
        elif tokens[index]['type'] == 'PLUS':
            token = {'type': 'PLUS'}
            index += 1
        elif tokens[index]['type'] == 'MINUS':
            token = {'type': 'MINUS'}
            index += 1
        else:
            print 'Invalid syntax'
        tokens2.append(token)   
    return tokens2



def evaluate(tokens): # + - calculate
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokens2 = md_evaluate(tokens)
    answer = evaluate(tokens2)
    print "answer = %f\n" % answer
