user_input = input("Enter numbers separated by space: ")

if not user_input.strip():
    print("No input provided")
    exit()

user_input = list(map(int, user_input.split()))

summ = 0
minn = user_input[0]
maxx = user_input[0]

for i in user_input:
    summ += i
    if i < minn:
        minn = i
    if i > maxx:
        maxx = i

meann = summ / len(user_input)

print(f"sum: {summ}, mean: {meann}")
print(f"min: {minn}, max: {maxx}")
