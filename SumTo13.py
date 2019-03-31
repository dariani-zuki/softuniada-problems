numbers =list(map(int, input (). split ()))
total = numbers[0]+numbers[1]+numbers[2]

checker=False

if total ==13:
    checker=True
    print ("Yes")
else:
    for i in range(len(numbers)):
        numbers[i]=numbers[i]*(-1)
        if checker:
            break
        for k in range(len(numbers)):
            numbers[k]=numbers[k]*(-1)
            if checker:
                break
            for j in range(len(numbers)):
                numbers[j]=numbers[j]*(-1)
                total = numbers[0]+numbers[1]+numbers[2]
                if total==13:
                    checker = True
                    print("Yes")
                    break
if not checker:
    print("No")                
