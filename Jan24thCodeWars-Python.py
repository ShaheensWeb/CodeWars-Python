#Problem set 7 Python
#Easy problem, maybe im just getting smarter
''' Finish the solution so that it sorts the passed in array of numbers. 
If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return [] '''

#Problem set 7 solution
def solution(nums): #solution = func name, nums = parameter input
    return sorted(nums) if nums else [] #if nums equals a non empty set, 
    									#it returns sorted(nums) otherwise, the empty set for nil/null/empty cases