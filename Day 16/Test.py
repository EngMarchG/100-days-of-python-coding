# Arr = [2, 4 , 5,6]
# print(Arr.index(5))
'''
class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        num2 = self.nums
        i = 0
        for num in nums:
            while i != len(nums):
                for Num in num2:
                    if Num == num:
                        pass
                    elif Num != num:
                        Num += num
                        if Num == target:
                            Num -= num
                            Num = num2.index(Num)
                            num = nums.index(num)
                            break
                break
            return Num, num
        
nums = []
numbers = input("Insert the numbers you want to add in the list: ")
idk = numbers.split(", ")
for char in idk:
    nums.append(int(char))
target = int(input("Input the requested target"))
nums = Solution.twoSum(nums, target)
'''

import random
import math

list = []
for n in range(150001):
    list.append(n)
i = 0 #run 1000 times
listo = []

while i < 10000:
    to_guess = random.choice(list)
    npc_guess = len(list)/2
    numberdown = 0
    numberup = len(list)
    counter = 1
    # print(npc_guess)
    i += 1
    while npc_guess != to_guess:
        if npc_guess > to_guess:
            numberup = npc_guess
            average = (numberup + numberdown)*0.5
            npc_guess = round(average)
            counter +=1
            if counter > 100:
                break
        elif npc_guess < to_guess: 
            numberdown = npc_guess
            average = (numberup + numberdown)*0.5
            npc_guess = round(average)
            counter +=1
            if counter > 100:
                break
        else:
            break

    #print(f"It took {counter} time to complete the number was {to_guess} and we reached {npc_guess}")
    listo.append(counter)

print(listo)
print(sum(listo)/len(listo))