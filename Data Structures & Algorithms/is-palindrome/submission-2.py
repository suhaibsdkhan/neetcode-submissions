class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first convert the string to a new string with only alphanumeric letters/numbers

        newstring=""

        for i in s:
            if i.isalnum():
                newstring+=i.lower()

        return newstring==newstring[::-1]