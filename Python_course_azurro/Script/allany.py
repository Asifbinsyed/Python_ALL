is_connected= True
has_electricity=True
has_paid= True
#this works for the boolean. it ensures that all the booleans are true. 
has_internet= all([is_connected, has_paid, has_electricity])


#any function performs check atleast one item is true. 

has_internet=any([is_connected, has_paid])

#you get a boolean return from these two inbuilt functions. 