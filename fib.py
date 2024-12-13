def longest_palindrome(word):
    def expand_around_center(left,right):
        while left>=0 and right<len(word) and word[left]==word[right]:
            left-=1
            right+=1
            return word[left+1:right]
    longest=" "   
    for i in range(len(word)):
        odd_palindrome=expand_around_center(i,i)
        even_palindrome=expand_around_center(i,i+1)
        #longest=max(longest,odd_palindrome,even_palindrome,key=len)
        if len(odd_palindrome)>len(longest):
            longest=odd_palindrome
        #if len(even_palindrome>len(longest)):
            longest=even_palindrome
        return longest
word="bananas"
result=longest_palindrome(word)
print("palindrome=",result)