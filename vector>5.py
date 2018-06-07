def scavec(vector):

    j = len(vector)
    for i in range(j):
        while(vector[i] < 6):
         vector[i] += 1
    return vector

vector = [11,3,2]

result = scavec(vector)

print(result)
