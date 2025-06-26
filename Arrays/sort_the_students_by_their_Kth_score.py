"""
Problem: Sort the Students by Their Kth Score
LeetCode: https://leetcode.com/problems/sort-the-students-by-their-kth-score/
Category: Array, Sorting
"""

from typing import List
#Bubble sort approach
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(score) - 1):
            for j in range(i, len(score)):
                if score[i][k] < score[j][k]:
                    score[i], score[j] = score[j], score[i]
        return score


if __name__ == "__main__":
    # Sample test case
    score = [[10, 6, 9], [7, 5, 11], [4, 8, 3]]
    k = 2
    sol = Solution()
    print(sol.sortTheStudents(score, k))
    # Expected output: [[7, 5, 11], [10, 6, 9], [4, 8, 3]]
