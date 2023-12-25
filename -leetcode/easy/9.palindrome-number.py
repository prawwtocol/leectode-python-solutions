#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome1(self, x: int) -> bool:
        """
        11511/11511 cases passed (50 ms)
        Your runtime beats 90.67 % of python3 submissions
        Your memory usage beats 5.13 % of python3 submissions (17.2 MB)
        """
        return str(x) == str(x)[::-1]

    def isPalindrome(self, x: int) -> bool:
        """
        Time complexity: O(log(n)) because we divided 10 in every iteration
        Space complexity: O(1)

        11511/11511 cases passed (44 ms)
        Your runtime beats 97.52 % of python3 submissions
        Your memory usage beats 5.13 % of python3 submissions (17.5 MB)
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # divide until half length
        # what if odd number of digits??
        a = 0
        while (a < x):
            x, a = x // 10, a * 10 + x % 10

        return a == x or a // 10 == x
# @lc code=end

Solution().isPalindrome(121)
