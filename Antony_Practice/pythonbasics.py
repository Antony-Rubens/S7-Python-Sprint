name = "antony"
age = 10
score = 80
print(name,age) 
if score >= 90:
    print(name)
elif score == 80:
    print(age)
else:
    print("sucess")
for i in range(5):
    print("help")
count = 0
while count < 3:
    print("hi")
    print(count)
    count += 1
#for inputing in python:
# Grabs the input as a string, then instantly converts it to an integer
x = int(input())
# input().split() breaks "10 20" into ["10", "20"]
# map(int, ...) converts both to integers
a, b = map(int, input().split())
