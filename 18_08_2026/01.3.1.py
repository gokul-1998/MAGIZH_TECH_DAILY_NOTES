# list comprehension

# nums=[]
# # 1-10 both included
# for i in range(1,11):
#     nums.append(i)

# print(nums)

print([i for i in range(1,11)])
print([i for i in range(1,11) if i%2==0])
print([i for i in range(1,11) if i%2==1])

# odd nums multiply by 2, even numbers mutiply by 3

print([i*2 if i%2==1 else i*3 for i in range(1,11)])
