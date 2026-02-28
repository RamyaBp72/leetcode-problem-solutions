class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        res = []

        x = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= x[1]:
                x = [x[0], max(x[1], intervals[i][1])]
            else:
                res.append(x)
                x = intervals[i]
        res.append(x)
        return res

