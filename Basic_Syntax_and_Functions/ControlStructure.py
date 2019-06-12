print('Python'<'python')
for c in "Python":
    print(c,end=',')
print("\n")
print(",".join('Python'))

while True:
    s=input('Please enter some Chinese:')
    if s=='退出':
        break
    elif s=='这个不算':
        continue
    for c in s:
        if c=='新':
            break
        print(c,end='')
    print('')
print("The program ends.")

