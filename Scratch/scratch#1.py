dict = {
    'meow':[1,2,3],
    "moo":["sound of cows","lavash kiri"],
    (1,2):"amazing tuple",
    69: "an intresting number",
    6.9:('byekhud float?',),
    
}

for key in dict.keys():
    print(type(key),type(dict[key]),sep="--->>>")
for key,values in dict.items():
    print(values,"is image of ",key)

dict2 = {
    1:[1,2,3],
    2:[4,5,6],
    3:[7,8,9]
    }
    
print(dict2[1].append(8))    
print(dict2[1])
a = 4
if(a not in dict2):
    dict2[a]=[3]
print(dict2)
for key, value in dict2.items():
    print(key,"---> ",value)


    
    

    

