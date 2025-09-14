class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        temp=x
        while(temp>0):
            r=temp%10
            rev=rev*10+r
            temp//=10
        if(x==rev):
            return True
        else:
            return False
        