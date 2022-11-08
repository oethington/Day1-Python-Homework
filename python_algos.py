# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

# cube = 1
# while cube<=1000:
#     num=cube**3
#     print(num)
#     if num == 1000:
#         break
#     cube += 1

# Get first prime numbers up to 100

# import math

# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, int(math.sqrt(num))+1):
#             if(num % i) ==0:
#                 break;
#         else:
#             print(num)

# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


# age_question = int(input("How old are you? "))

# def howOld(age_question):
    # passed through a funtion on VS code. But tested the input on jupiter. 

#     if age_question < 18:
#         print("kid")
#     if age_question in range(18, 65):
#         print("adult")
#     else:
#         print("seniors")
    
    #Calling the function 
# howOld(18)