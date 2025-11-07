# # i = 0 
# # while i <= 10 :
# #     print(i)
# #     i = i + 1


# # for value in range():
#     # code to be executed 


# # range(start,stop,step)

# # for i in range(10,0,-1):
# #     print(i)

# # sum


# # sum = 0 
# # for i in range(1,11):
# #    sum += i
# # print(sum)

# # factorial of a number

# # 5 - 1x2x3x4x5

# num = int(input('enter your num:-'))


# fact = 1
# for i in range(1,num+1):
#     fact*=i

# print(fact)


# find sum and average of n numbers 

# n = how many numbers 3

# neter number 1
# neter number 2
# neter number 3

# sum 6 
# average 2

# 3 

# 10
# 20
# 30

# 60

# 20


# count = int(input('how many numbers : - '))
# sum = 0 
# for i in range(count):
#    b = int(input('enter your number: -'))
#    sum = sum +b
# print('sum',sum)
# print('average',sum/count)



# pass , break , continue 

# age = 19

# if age > 18:
#     pass
# print(age)


# break and continue  loops 



# for i in range(1,11):
#     print(i)
#     if i == 5:
#         break

# print('mohan')

# for i in range(1,11):
#     if i % 3 == 0:
#         continue
#     print(i)



# name = 'mohan'

# if name == 'mohan':
#     pass



# for i in  range(1,11):
#     if i % 2 == 0:
#         print(i)

# # for i in range(1,11):
# #     if i % 2 != 0:
# #         continue
# #     print(i)

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

# # check if a number is prime or not 


num = int(input('enter a number : - '))
is_prime = True
if num == 1:
   is_prime = False
else:
    for i in range(2,num):
        if num % i == 0 :
          is_prime = False
          break

if is_prime == True:
    print('prime')
else:
    print('not a prime')