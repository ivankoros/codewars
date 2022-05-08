# find the difference between two arrays

def array_diff(a, b):
    newArray = []
    for i in a:
        if i not in b:
            newArray.append(i)
    return(newArray)