#driver (Amro Hijaz) {U44065831} (50%)
#Navigator (Adam Bricha) {U9233585} (50%)

#This program asks the user to input any amount of numbers of there choosing
#the program will then ask for a limit
#The output will tell the user which numbers are less then the limit



def fun(arr, limit):

    count = 0
    n = len(arr)

    for i in range(n):
        if arr[i]< limit:
            count+=1

    if count==0:
        print(f"No input number is less than limit {limit}")
    else:
        for i in range(n):
            if arr[i]< limit:
                print(arr[i], end=" ")
        if count == 1:
            print(f"is less than the limit {limit}")
        else:
            print(f"are less than the limit {limit}")
def main():
    n = int(input("How many numbers will you compare? "))
    arr=[]
    temp = 0
    for i in range(n):
        temp = int(input("Enter a number: "))
        arr.append(temp)
    limit = int(input("What is the limit? "))
    fun(arr, limit)
if __name__=="__main__":
    main()