#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import Dict, List, Set


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        61/61 cases passed (2250 ms)
        Your runtime beats 34.14 % of python3 submissions
        Your memory usage beats 85.91 % of python3 submissions (17 MB)
        """
        # O(n^2)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i + 1 :]):
                # j = 0 and
                # actual index is
                # i + 1
                if x + y == target:
                    return [i, i + 1 + j]
        return []  # for mypy check

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        61/61 cases passed (70 ms)
        Your runtime beats 49.31 % of python3 submissions
        Your memory usage beats 7.65 % of python3 submissions (18.9 MB)
        """

        # use hashing
        hash_table = set()
        #  set uses hashMap https://stackoverflow.com/questions/3949310/how-is-set-implemented/3949350#3949350 # noqa
        #  {} creates a dict
        index_hash_table: Dict[int, List[int]] = dict()
        iht = index_hash_table  # creates an alias
        for i, x in enumerate(nums):
            hash_table.add(x)
            if x not in iht.keys():
                iht[x] = [i]
            else:
                iht[x].append(i)
        for i, x in enumerate(nums):
            if target - x in hash_table:
                if x == target - x:
                    # probablility of repeating element
                    ihtx = iht[x]
                    if len(ihtx) >= 2:
                        # then choose different indicies
                        return [ihtx[0], ihtx[1]]
                    else:
                        # impossible, skip
                        pass
                else:
                    # TODO not very readable
                    return [iht[x][0], iht[target - x][0]]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ """
        hash_table: Set[int] = set()  # the set uses hash table
        index_hash_table: Dict[int, List[int]] = dict()
        # alias
        iht: Dict[int, List[int]] = index_hash_table

        for i, num in enumerate(nums):
            hash_table.add(num)
            if num not in iht.keys():
                iht[num] = [i]
            else:
                iht[num].append(i)

            if target - num in hash_table:
                if num == target - num:
                    # chance of repeating element
                    ihtx: List[int] = iht[num]
                    if len(ihtx) >= 2:
                        # then choose different indicies
                        # return [ihtx[0], ihtx[1]]
                        return ihtx[:2]
                    else:
                        # impossible, skip
                        pass
                else:
                    return [iht[num][0], iht[target - num][0]]
        return []


# @lc code=end
