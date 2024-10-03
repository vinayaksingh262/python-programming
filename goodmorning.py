import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp1 =int( time.strftime('%H'))
print(timestamp1)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
if(timestamp1<4):
    print("good night")
elif(timestamp1>4):
    print("good morning")
elif(timestamp1>16):
    print("goo evening")
else:
    print("good night")