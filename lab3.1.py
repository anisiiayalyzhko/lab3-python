S = str(input("Enter a string with more than 12 symbols : "))

while (len(S) < 12):

    S = str(input("Enter another string, because this one contains less than 12 symbols: "))

print("Every second symbol from the 5th element of the word till the middle of it: ", S[4 : len(S)//2 : 2])