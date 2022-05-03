# https://leetcode.com/problems/find-the-duplicate-number/
count = {}
for num in nums:
  if num not in nums:
    count[num] = 1
  else:
    count[num] += 1
 for key,value in count.items():
  if value>1:
    return key
return -1
