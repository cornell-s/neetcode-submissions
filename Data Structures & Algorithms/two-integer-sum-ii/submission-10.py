class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 

        while l < r:
            total = numbers[l] + numbers[r]

            if target == total:
                break
            elif target > total:
                l = l + 1
            else:
                r = r - 1

        return [l + 1, r + 1]