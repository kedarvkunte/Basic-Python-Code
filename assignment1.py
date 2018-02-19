##################################################
# PROBLEM 1: Filtering even numbers
##################################################
# Fill in the body of the following function, evens_only.
# The function takes one argument, a list of numbers (float 
# or integer). You should write code so that evens_only 
# returns a list containing only the even, integer valued
# numbers from this list. The returned list must also 
# satisfy the following conditions:
#   1) The data type of all numbers in the returned list
#      should be Integer.
#   2) The numbers in the returned list should be in the 
#      same order as in input_list.
#
# For example, evens_only([1,2,2.5,3,4]) should return the 
# list [2,4].

def evens_only(input_list):
    ### Add your code here ###
    """ Function to return the even integers in the same order as that of list"""
    even_integer_list = []
    
    for i in input_list:
       if(i%2 ==0):
            even_integer_list.append(int(i))

    return even_integer_list

#input_list = [1,1.5,2.3,4.0,4.6,5,5,7,7.2,8,8.9]
input_list = []
cap = input("Enter the capacity of the list: ")
for i in range(int(cap)):
    print("Number ", i + 1)
    input_number = input("Enter the number: ")

    input_list.append(float(input_number))

print("The even integers in input list in the same order  are\n",evens_only(input_list))






    ##################################################
    # PROBLEM 2: Piecewise function
    ##################################################
    # Fill in the body of the function piecewise that takes
    # a single float argument and returns the function
    # defined in the assignment handout, F(x). The data
    # type of the retruned value should be float.



def piecewise(x):
    #pass
    
    if x<0:
        return(float(-1))
    elif (x>=0) and (x<2):
        return(float(3*(x**2)))
    else:
        return(float(-1*x))
    
#x=5
x= input("\n Enter an Integer or Float Value for piecewise function f(x):  ")
f_x = piecewise(float(x))
print("For given x = ",x," F(x) = ",f_x,"\n")


    ##################################################
    # PROBLEM 3: Character count
    ##################################################
    # Fill in the body of the function character_count.
    # character_count takes a string file_path, reads in
    # the text file at file_path as a string, and counts the
    # number of times each alphabetic character (a
    # through z) appears in the file. character_count
    # should return a dictionary that maps each letter
    # that appears at least once in the string to its
    # count. The keys of this dictionary should have type
    # string and the values should have type int.

import string



def character_count(input_file_name):


    #alphabets_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    file_path = open(input_file_name, "r")
    input_string = file_path.read()
    modified_string = input_string.lower()

    character_Count_dict = dict()

    def addCharacter_Count(character, count):
        character_Count_dict[character] = count

    list_atoz = string.ascii_lowercase[:26]

    for i in range(26):
        if modified_string.count(list_atoz[i]) > 0:
            addCharacter_Count(list_atoz[i], modified_string.count(list_atoz[i]))

    file_path.close()
    return character_Count_dict


dict1 = character_count("test1.txt")
print("\nCorresponding Character count in Dictionary 1 is \n",dict1,"\n\n")



dict2 = character_count("test2.txt")
print("\nCorresponding Character count is \n",dict2,"\n\n")



dict3 = character_count("test3.txt")
print("\nCorresponding Character count is \n",dict3,"\n\n")


