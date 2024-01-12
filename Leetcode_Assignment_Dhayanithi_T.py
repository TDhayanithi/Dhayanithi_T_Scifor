#!/usr/bin/env python
# coding: utf-8

# ### 1.  Merge Strings Alternately
# * You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# 
# * Return the merged string.

# In[1]:


class Solution(object):
    def mergeAlternately(self, word1, word2):
        M = []
        i, j = 0, 0
        while (i < (len(word1)) and j < (len(word2))):
            M += [word1[i], word2[j]]
            i += 1
            j += 1
        M += word1[i:]
        M += word2[j:]
        return ''.join(M)

solution = Solution()
print(solution.mergeAlternately('Da','hyanithi')) 


# ### 2. Find the Difference
# * You are given two strings s and t.
# 
# * String t is generated by random shuffling string s and then add one more letter at a random position.
# 
# * Return the letter that was added to t.

# In[2]:


from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        c_s = Counter(s)
        c_t = Counter(t)
        diff = c_t - c_s
        return diff.popitem()[0]
solution = Solution()
print(solution.findTheDifference('Dhaya','Dhayan'))


# ### 3. Find the Index of the First Occurrence in a String
# * Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# In[3]:


class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  
print(solution.strStr("leetcode", "leeto"))  


# ### 4. Valid Anagram
# * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# 

# In[4]:


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        c_s = {char: s.count(char) for char in s}
        c_t = {char: t.count(char) for char in t}
        return c_s == c_t
solution = Solution()
print(solution.isAnagram('anagram','nagaram'))


# ### 5. Repeated Substring Pattern
# * Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# In[5]:


class Solution(object):
    def repeatedSubstringPattern(self, s):
        return any(s[:i] * (len(s)//i) == s for i in range(1, len(s)//2 + 1))

solution = Solution()
print(solution.repeatedSubstringPattern("abab")) 


# ### 6. Move Zeroes
# * Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# * Note that you must do this in-place without making a copy of the array.

# In[6]:


class Solution(object):
    def moveZeroes(self, nums):
        ins = 0
        for num in nums:
            if num != 0:
                nums[ins], num = num, nums[ins]
                ins += 1

        while ins < len(nums):
            nums[ins] = 0
            ins += 1

solution = Solution()
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(nums1) 


# ### 7. Plus One
# * You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# 
# * Increment the large integer by one and return the resulting array of digits.

# In[7]:


class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

solution = Solution()
print(solution.plusOne([1, 2, 3]))  


# ### 8. Sign of the Product of an Array
# * There is a function signFunc(x) that returns:
# * 1 if x is positive.
# * -1 if x is negative.
# * 0 if x is equal to 0.
# * You are given an integer array nums. Let product be the product of all values in the array nums.
# * Return signFunc(product).

# In[8]:


class Solution(object):
    def arraySign(self, nums):
        count_negative = 0

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                count_negative += 1

        return 1 if count_negative % 2 == 0 else -1

# Example usage:
solution = Solution()
print(solution.arraySign([-1, -2, -3, -4, 3, 2, 1]))  


# ### 9. Can Make Arithmetic Progression From Sequence
# * A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# * Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

# In[9]:


class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        common_diff = arr[1] - arr[0]
        
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != common_diff:
                return False
        return True

solution = Solution()
print(solution.canMakeArithmeticProgression([3, 5, 1]))


# ### 10. Monotonic Array
# * An array is monotonic if it is either monotone increasing or monotone decreasing.
# 
# * An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# 
# * Given an integer array nums, return true if the given array is monotonic, or false otherwise.

# In[12]:


class Solution(object):
    def isMonotonic(self, nums):
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
            if nums[i] > nums[i - 1]:
                decreasing = False

        return increasing or decreasing

solution = Solution()
print(solution.isMonotonic([1, 2, 2, 3]))


# ### 11. Roman to Integer
# * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# 
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# * For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# 
# * Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# 
# * I can be placed before V (5) and X (10) to make 4 and 9. 
# * X can be placed before L (50) and C (100) to make 40 and 90. 
# * C can be placed before D (500) and M (1000) to make 400 and 900.
# * Given a roman numeral, convert it to an integer.

# In[13]:


class Solution(object):
    def romanToInt(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0

        for char in s:
            current_value = roman_dict[char]

            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            prev_value = current_value

        return total

solution = Solution()
print(solution.romanToInt("III"))   


# In[ ]:



