def scavec(vector,scalar):

    b = []
    for i in vector:
         b.append(i * scalar)

    return b

vector = [2,4,6]
scalar = 3

result = scavec(vector,scalar)

print(result)
