
def average_grades (x: dict[str,list[int]]) -> dict[str,float]:
    y = {}
    for avg in x:
        total = 0 
        for grade in x[avg]:
            total += grade
            y[avg] = total/len(x[avg])
    return y

def vowels_and_threes(x:str)-> str:
    strng: str = ""
    i = 0 
    if i % 3 == 0 and x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
        i +=1 
    elif i % 3 == 0 or x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
        strng += x[i]
        i +=1
    else:
        i += 1 
    return strng


def vowels_and_threes(x:str)-> str:
    new_string = ""
    i = 0 
    while i < len(x):
        if i % 3 == 0 and (x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u'):
            new_string += "" 
        elif i % 3 == 0:
            new_string += x[i]
        elif x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u':
            new_string += x[i]
        i +=1 
    return new_string

print(vowels_and_threes("hello world"))
print(vowels_and_threes("aeiou"))
            

def concat(x:list[int], y: list[int])-> list[int]:
    xy = []
    i = 0  
    j = 0
    while i < len(x):
        xy.append(x[i])
        i += 1 
    while j < len(y):
        xy.append(y[j])
        j += 1 
    return xy 

print(concat([1,2,3],[2,3,4]))



def invert(x: dict[str, str]) -> dict[str, str]:
    """This function takes in a dictionary and inverts it."""
    new_dict = {}
    for key in x:
        new_dict[x[key]] = key
    return new_dict

print(invert({'a': 'z', 'b' : 'y', 'c': 'x'}))


def b(x:list[int], y: list[int])-> bool:
    i = 0 
    hello: bool = True 
    while i < len(x):
        if x[i] != y[i]:
            hello = False
        else: 
            hello = True 
        i += 1 
    return hello 

print(b([0,1,2],[0,3,2]))

def k(x:dict[str,str])-> int:
    em = {}
    for key in x:
        if x[key] in em:
            em[x[key]] += 1
        else:
             em[x[key]] = 1

        for key in em:
            max = 0
            if em[key] > max:
                max = em[key]
    return max 

print(k({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def subset(x: dict[int,str],y:list[int]) -> dict[int,str]:
    em = {}
    for item in y:
        if item in x:
            em[item] = x[item]
        else:
            em = {}
    return em

letter: dict[str,int] = {1:"a",2:"c",3:"d"}
for value in letter:
    print(value)




print(len(letter))

print(subset(letter, [3]))

print(letter.pop(letter{1]))


