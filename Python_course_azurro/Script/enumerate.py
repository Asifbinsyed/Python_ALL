#enumerate helps you to put an index

names: list[str]= ['robert', 'asif', 'messi']
for name in names:
    print(names.index(name)+1, ':' + name)
    
# this is a more manual approach. you can achieve this using enumerate function. 

for index, name in enumerate(names):
    print(index+1,':', name)
    
#if you use only one item in each loop then you will get a tuple

for index in enumerate(names, start=1):
    print(index)