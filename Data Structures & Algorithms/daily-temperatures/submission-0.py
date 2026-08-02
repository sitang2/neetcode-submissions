class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # array = temperatures
        # temperatures[i] = degree on (i)th day
        # result = [] and result[i] = day that warmer than ith day

        N = len(temperatures)
        result = [0] * N
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([temp, i])
        return result
