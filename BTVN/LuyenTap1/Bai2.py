from itertools import product
def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

def check(strNumber, target):
    count = 0
    listNumbers = list(splitter(strNumber))
    operators = ['+', '-', '*']
    for numbers in listNumbers:
        operations = product(operators, repeat = len(numbers) - 1)
        numbers_ = list(map(str, map(int, numbers)))
        for operation in operations:
            operation = list(operation)
            
            operation = operation + [' ']
            
            function = ' '.join(x + y for x, y in zip(numbers, operation))
            function_ = ' '.join(x + y for x, y in zip(numbers_, operation))
            if function == function_:
                try:
                    if eval(function) == target:
                        count += 1
                except:
                    continue
    return count
strNumber = input().strip()
target = int(input().strip())

print(check(strNumber, target))
