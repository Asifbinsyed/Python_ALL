status: int = 400

if status == 401: 
    print('Bad Request')
    
elif status == 402: 
    print('Forbidden')
    
elif status == 404: 
    print('site not found')
    
else: 
    print('something wrong')
    


# By using the match and case, you can achieve same feat with cleaner code.

match status:
    case 401:
        print("Bad request")
    case 402:
        print("Forbidden")
    case 404:
        print("site not found")
    case _:
        print("something wrong")
    case 401: 
        print("Bad request ")
    
    case 402: 
        print("Forbidden")
        
    case 404: 
        print(" site not found")
    
    case _: 
        print("Something went wrong")
        
# the best case for this match case is using it for string 
user_input = input('Command: ')
p_command = user_input.split()
print(p_command)

match p_command:
    case ['find' ,*images]: 
        print(f'finding: {images}')
        
    case _: 
        print("Command not recognized")