stack = []

stack.append (10)
stack.append(20)
stack.append(30)
stack.append(40)

print("stack:", stack)

#  Peek 

print("stack : ", stack[-1])

#  Remove element

removed = stack.pop()

print("Removed element :", removed)
print("Updated stack:", stack)

