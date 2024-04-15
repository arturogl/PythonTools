class Container:
    def __init__(self):
        self.numbers = set()

    def add(self, value: int) -> str:
        self.numbers.add(value)
        return ""

    def exists(self, value: int) -> str:
        if value in self.numbers:
            return "true"
        else:
            return "false"

def solution(queries):
    container = Container()
    answers = []
    for operation, value in queries:
        value = int(value)
        if operation == "ADD":
            container.add(value)
            answers.append('')
        elif operation == "EXISTS":
            answers.append(container.exists(value))
    return answers

# Example usage:
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"]
]

# print(process_queries(queries))  # Output: ['true', 'true', 'true', 'false', 'false', 'true']

L = solution(queries)

print('[', end='') #just to print the opening third bracket [
for i in range(len(L)): #the variable i will assume the values from 0 to length of L - 1 i.e. the indices of the elements
    print('"' + L[i] + '"', end='') #display a double quote and the string inside it
    if i < len(L)-1:
        print(',', end=' ') #if i is not the index of the last element then display a comma after it
print(']') #just to print the closing third bracket ]
