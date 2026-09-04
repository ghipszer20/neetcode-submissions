"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    # Optimal solution: sorting, compare adjacents (O(nlogn) time, O(1) space)
    def canAttendMeetings(self, intrvs):

        intrvs.sort(key = lambda i : i.start)

        for i in range(1, len(intrvs)):
            if intrvs[i].start < intrvs[i-1].end:
                return False

        return True

    # Base Case: O(n^2) time, O(1) memory
    # def canAttendMeetings(self, intrvs: List[Interval]) -> bool:
    #     for i in range(len(intrvs)):
    #         for j in range(i + 1, len(intrvs)):
    #             if intrvs[j].start < intrvs[i].end and intrvs[j].end > intrvs[i].start:
    #                 return False
        
    #     return True
                    