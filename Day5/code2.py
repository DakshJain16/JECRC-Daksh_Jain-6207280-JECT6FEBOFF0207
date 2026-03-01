'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You 
can return the answer in any order

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

def twoSum(coll, target):
    for i in range(len(coll) - 1):
        for j in range(i + 1, len(coll)):
            if coll[i] + coll[j] == target:
                return [i , j]
    
    return -1

#print(twoSum([11, 15, 2, 7], 9))

l = int(input("Enter the length of collection: "))
coll1 = []
print("Enter the elements: ")
for x in range(l):
    a = int(input())
    coll1.append(a)

tar = int(input("Enter target: "))
print(twoSum(coll1, tar))