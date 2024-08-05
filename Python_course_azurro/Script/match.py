status: int = 400

if status == 401: 
    print('Bad Request')
    
elif status == 402: 
    print('Forbidden')
    
elif status == 404: 
    print('site not found')
    
else: 
    print('something wrong')