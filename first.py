#! /bin/Python3

#print("Learning bash Scripting")

# def Caleb ():
#     name = input("Whats your name Hacker? ")
#     if name:
#         print("Do you wanna learn hacking ?",name)
#         answer = input ("Enter your answer (Yes or No): ")
#         ans = answer.capitalize()
#         if ans == "Yes" or ans == "YES":
#             print("Welcome to my hacking class",name)
#         else:
#             print("Get lost!!")
# Caleb()

def MyList ():
    crushes = ["michell","Natasha","stephanie","christine","chocolate neighbour","waiter"]
    # print(crushes[1:4])
    # print(crushes[-1])
    # print(crushes[1:])
    # print(crushes[:1])
    # print(crushes[:])
    #crushes.append("Debbie")
    #crushes.pop() #removes the last value on the last index
    #crushes.insert(0,"debbie")
    crushes.pop(0) # removes the value on index 0
    print(crushes[:])#prints item on index 0
MyList()
