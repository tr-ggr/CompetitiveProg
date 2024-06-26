#Most Frequent Even Element
def MostFrequentEvenElement():
    n = int(input("Enter the number of integers: "))
    print(f"Enter {n} integers")
    nums = []
    for i in range(n):
        nums.append(int(input()))

    max_num, max_count = 0, 0
    for num in nums:
        if num % 2 == 0:
            m = nums.count(num)
            if m > max_count or (
                m == max_count and 
                num < max_num
            ):
                max_num = num
                max_count = m

    return max_num

#First Letter to Appear Twice
def FirstLetterToAppearTwice():
    strs = str(input("Enter a string: "))

    for i in range(len(strs) - 1):
        if strs[i] == strs[i+1]:
            c = strs[i] 
            break

    print(f"The final letter to appear twice is: {c}")

#SmallestMultipleThatIsEven
def SmallestMultipleThatIsEven():
    n = int(input("Enter a positive integer: "))
    n = n if n % 2 == 0 else n * 2

    print(f"Results: {n}")

# FirstLetterToAppearTwice()
SmallestMultipleThatIsEven()
# print(f"Most Frequent Even Element: {MostFrequentEvenElement()}") 

    