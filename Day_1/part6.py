for i in range(5):
    print(i)

scores=[70,85,60,90,45]

for score in scores:
    print("Score: ",score)

count =1
while count <=5:
    print(count)
    count +=3



scores = [45,70,85,30,90,55]

total=0

for score in scores:
    total += score

average = total / len(scores)

pas=0
fail=0
for score in scores:
    if score>=40:
        pas+=1
    elif score<=40:
        fail+=1

print("Number of pass: ",pas)
print("Number of fail: ",fail)
print("Total: ",total)
print("Average: ",average)