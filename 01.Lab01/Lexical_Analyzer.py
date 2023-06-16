with open(r"01.Lab01\01.input_Lab01.txt") as f:
    code = f.readlines()

keywords = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally', 'float', 'for', 'if', 'implements', 'import', 'instanceof', 'int', 'interface', 'long', 'native', 'new', 'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp', 'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while']
math_operators = ['+', '-', '*', '/', '%', '=']
logical_operators = ['<', '>', '<=', '>=', '==', 'and', 'or']
numerical_values=['0','1','2','3','4','5','6','7','8','9']
others = [',', ';', '(', ')', '{', '}', '[', ']']

keyword_outputs = []
math_operator_outputs = []
logical_operator_outputs = []
numerical_outputs = []
identifier_outputs = []
other_outputs = []



for line in code:
    line = line.strip().split()
    
    for token in line:
        if token in keywords: keyword_outputs.append(token) # else, if stuff
        elif token in math_operators: # + - =
            if token not in math_operator_outputs: math_operator_outputs.insert(0, token) # reverse append || math_operator_outputs.append(token[::-1]) 
        elif token in logical_operators: logical_operator_outputs.append(token) #> <
        elif token[-1] in others:
            # print(token[-1])
            if token[-1] not in other_outputs: other_outputs.append(token[-1])

            if len(token) > 1: # to remove ',' in the last identifier
                # print("Left data", token[0], token[-1])
                if token[0] in numerical_values:
                    # print(token[:-1])
                    if token[:-1] not in numerical_outputs: numerical_outputs.append(token[:-1])
                else:
                    if token[:-1] not in identifier_outputs: identifier_outputs.append(token[:-1])

def print_output(category, output_list, separator=' '):
    print(f'{category}: {separator.join(output_list)}')

print_output('Keywords', keyword_outputs, ', ')
print_output('Identifiers', identifier_outputs, ', ')
print_output('Math Operators', math_operator_outputs, ', ')
print_output('Logical Operators', logical_operator_outputs, ', ')
print_output('Numerical Values', numerical_outputs, ', ')
print_output('Others', other_outputs)