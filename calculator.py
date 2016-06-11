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


def md_evaluate(tokens): # * / calculate
    tokens2 = []
    index = 0

    while index < len(tokens):

        if tokens[index]['type'] == 'NUMBER':
            
            number = tokens[index]['number']

            print number

            if index == len(tokens)-1:
                print 'last number'
                token = {'type': 'NUMBER', 'number': number}
                index += 1

            else:
                while tokens[index+1]['type'] in {'MULTI', 'DIVIS'}:
                    print 'exit * or /'
                    index += 2
                    if tokens[index-1]['type'] == 'MULTI':
                        number = number * tokens[index]['number']
                    else:
                        number = number*1.0/tokens[index]['number']

                    if index >= len(tokens)-1:
                        break;
                     
                token = {'type': 'NUMBER', 'number': number}
                index += 1

        elif tokens[index]['type'] in {'PLUS', 'MINUS'}:

            print 'Plus or Minus'
            
            token = {'type': tokens[index]['type']}
            index += 1

        else:
            print 'Invalid syntax'

        tokens2.append(token)
        
    return tokens2



def evaluate(tokens): # + - calculate
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1

    tokens2 = md_evaluate(tokens)
    
    while index < len(tokens2):
        
        if tokens2[index]['type'] == 'NUMBER':
            
            if tokens2[index - 1]['type'] == 'PLUS':
                answer += tokens2[index]['number']
                
            elif tokens2[index - 1]['type'] == 'MINUS':
                answer -= tokens2[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print "answer = %f\n" % answer
