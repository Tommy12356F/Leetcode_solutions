class Solution(object):
    def reverseVowels(self,s):
        s = list(s)
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        V = []
        I = []
        
        # Collect vowels and their indices
        for i in range(len(s)):
            if s[i] in vowels:
                V.append(s[i])
                I.append(i)
        
        # Reverse the vowels list
        V.reverse()
        
        # Replace vowels with reversed ones
        for i in range(len(I)):
            s[I[i]] = V[i]
        
        return "".join(s)


