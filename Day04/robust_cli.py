def read_numbers()->list[int]:
    user_input=input("enter input with spaces:")
    if not user_input.strip():
        print("No input provided")
        exit()
    user_input=list(map(int,user_input.split()))
    return user_input
    
def compute_stats(numbers:list[int]):
    
    total=meann=0
    maximum=numbers[0]
    minimum=numbers[0]
    count=0
    for i in numbers:
        count+=1
        total+=i
        if i<minimum:
            minimum=i
        if i>maximum:
            maximum=i
    
    meann=total/count
    return total,meann,minimum,maximum,count
if __name__ == "__main__":
    user_input=read_numbers()
    total,meann,minimum,maximum,count=compute_stats(user_input)
    print(f"sum:{total}")
    print(f"mean:{meann}")
    print(f"min:{minimum}")
    print(f"max:{maximum}")
    print(f"count:{count}")
