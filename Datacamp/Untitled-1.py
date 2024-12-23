# %%
# the way you put condition on the comprehension 

[num**2 if num%2==0 else 0 for num in range(10)]

# %%
# we can also create dictionary comprehension 

pos_neg = {num: -num for num in range(9)}
print(type(pos_neg))

# %%
pos_neg

# %%
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Create dict comprehension: new_fellowship
new_fellowship = {members:len(members) for members in fellowship}
# Print the new dictionary
print(new_fellowship)

# %%
# Generator Expression : 
# difference between the generator expression and lists is that it doesn't store the list instead 
# actually an object which create list when needed. 

generator= (number**2 for number in range(5))

# %%
print(next(generator))

# %%


# Extract the clock time: tweet_clock_time
tweet_clock_time = [tweet_time[11:18] for entry in tweet_time]

# Print the extracted times
print(tweet_clock_time)

# %%
string= 'hello'
string[1:3]

# %%



