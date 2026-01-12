


def addition(x,y):
    return x + y

#usermathinput_x = int(input("x: "))

#usermathinput_y = int(input("y: "))



#print(addition(usermathinput_x,usermathinput_y))


def sqrt(numb,iterations):

    if numb <= 0:
        return "killl urself"

    aprox = numb/2
    for _ in range(iterations):
        aprox = (aprox + numb/aprox)/2 
    return aprox


    


    










# Make a function that passes in TWO arguements, x and y.
# the function should add x and y together and return the result
# example: add(x,y) would print the result of both passed in arguements
# print(add(5,7))
# 12






 
def meow(x,y):
    return sqrt(x,y)

#userInput = int(input("number"))
#asd = int(input("iterations"))


#print(meow(userInput,asd))





def string_combiner(x,y):
    return x + " " + y


string_1 = input("string 1: ")
string_2 = input("string 2: ")


print (string_combiner(string_1,string_2))

string_3 = input("string 3: ")
string_4 = input("string 4: ")

print (string_combiner(string_3,string_4))