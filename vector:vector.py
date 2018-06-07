def scavec(vector1,vector2):

    b = []
    j = len(vector1)
    for i in range(j):
         b.append(vector1[i]+vector2[i])

    return b

vector1 = [0,5,8]
vector2 = [1,2,3]

result = scavec(vector1,vector2)

print(result)
