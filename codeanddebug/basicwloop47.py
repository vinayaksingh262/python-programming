
# i=1
# count1,count2=0,0
# while i<=100:
#     if i%7==0:
#         count1+=1
    
#     elif i%6==0:
#         count2+=1
#     i+=1
# print(f'{count1} are divisible by 7 and {count2} are divisble by 6 from 1 to 100')

i = 1
count = 0


while i <= 200:
    
    if i % 6 == 0 and i % 7 == 0:
        count += 1
    i += 1

print(f"Total numbers divisible by both 6 and 7 between 1 and 200: {count}")

