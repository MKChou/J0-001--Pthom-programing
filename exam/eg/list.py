
#list

list  = [1, 2, '3', [4,5,6]]

print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[3][1])
print(list[3][2])

print("------ append使用 --------")
print("before:",list)
list.append(87)
print("after:",list)

print("------ pop使用 --------")
print("before:",list)
list.pop(0)
print("after:",list)