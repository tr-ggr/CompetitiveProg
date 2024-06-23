#Double Reversal
def reverseReverseN(n : int) -> bool:
    return n % 10 != 0

#Alternating Digit Sum
def AlternatingDigitSum(n : int) -> int:
    N, i, sum = str(n), 1, 0
    for num in N:
        sum += (int(num) * i)
        i *= -1

    return sum

#Percentage Of Letters In String
def PercentageOfLettersInString(s : str, c : chr) -> str:
    strlen = len(s)

    dict = {}

    for l in s:
        if l in dict:
            dict[l]+=1
        else:
            dict[l] = 1

    return str(f"{int((dict[c] / strlen) * 100)}%") 


print(reverseReverseN(1001))