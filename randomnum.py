import time
start=int(input('Enter starting num '))
end=int(input('Enter ending num '))
end+=1
x=int(time.time()*(10**6))
t=x%end
#print(t,x)
while t<start or t>=end:
    if t<start:
        t=t+start
    if t>=end:
        t=t%end
print(t)
