# Pranay Patel, 20CE098
# AIM: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and
# same frequency of each character. If there are odd number of characters in the string, we ignore the middle
# character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the
# same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes.
# Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
# Your task is simple. Given a string, you need to tell if it is a lapindrome.
# github link : https://github.com/PranayPatel1707/python-basic-problems
n = int(input())
str1 = ""
str2 = ""
for i in range(n):
    word = input()  # taking word
    length = len(word)  # taking its length
    mid = int(length/2)
    if(length%2==0):  # if number of alphabets are even in word
        str1 = word[:mid]
        str2 = word[mid:]
    else:  # if it is an odd number, we ignore the middle most element
        str1 = word[:mid]
        str2 = word[mid+1:]
    l1 = list(str1)
    l2 = list(str2)
    l1.sort()  # elements of word get arranged in order
    l2.sort()

    if(l1==l2):
        print("YES")
    else:
        print("NO")
