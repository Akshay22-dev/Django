# Print first 10 values
'''for i in range(10): 
    print(i)'''

'''for x in range(2, 6):
    print(x)'''

#Break loop when x is 3, and see what happens with the else bloc:
'''for x in range(6):
    if  x ==3 :
        break
    print(x)
else:
    print('finally finished!')'''

#Nested Loop

adj = ["red", "big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

