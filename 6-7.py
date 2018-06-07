def scavec(list,x): #function that computers scalar/vector product

    answer = 0        #scalar/vector product
    items = len(list)  #number of items in the list entered

    for i in range(items):  #performs computation of scalar and vector
        
        answer += x*list[i]

    return answer


print("Enter a list of numbers: ") #prompts user to enter a vector

list = [int(z) for z in input().split()] #loads vector entries into a list

x = int(input("Enter an integer: "))  #prompts user to enter a scalar

result = scavec(list,x)  #product of scalar and vector

print(result)           #displays product of scalar and vector
