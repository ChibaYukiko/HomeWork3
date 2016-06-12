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
    token = {'type': 'MULTI'}
    return token, index + 1

def readDivision(line, index): # read /
    token = {'type': 'DIVIS'}
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


def evaluateMultiplyAndDivide(tokens): # * / calculate
    tokens2 = []

    tokens.insert(0, {'type': 'MULTI'})　# Insert a dummy '*' token
    index = 1
    number = 1

    while index < len(tokens):

        if tokens[index]['type'] == 'NUMBER':
            
            if tokens[index-1]['type'] == 'MULTI':
                number = number * tokens[index]['number']
                #print number
                
            elif tokens[index-1]['type'] == 'DIVIS':
                number = number*1.0 / tokens[index]['number']
                #print number
                
            else : # tokens[index1]['type'] in {'PLUS', 'MINUS'}
                number = tokens[index]['number']
                #print number
            
                   
        elif tokens[index]['type'] in {'PLUS', 'MINUS'}:
            
            token1 = {'type': 'NUMBER', 'number': number}
            tokens2.append(token1)
            
            token2 = {'type': tokens[index]['type']}
            tokens2.append(token2)
                      
        index += 1
            
    # index >= len(tokens) last number
    token = {'type': 'NUMBER', 'number': number}
    tokens2.append(token)
       
    return tokens2



def evaluatePlusAndMinus(tokens): # + - calculate
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


def evaluate(tokens):

    tokens2 = evaluateMultiplyAndDivide(tokens)
    answer = evaluatePlusAndMinus(tokens2)

    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %f\n" % answer
