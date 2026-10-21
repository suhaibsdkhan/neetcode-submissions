class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if len(set(temperatures)) == 1:
            return [0] * n

        result = []

        for i in range (n -1):
            count = 1
            for r in range(i+1, n):
                if r == n-1 and temperatures[r] <= temperatures[i]:
                    result.append(0)
                    break
                if temperatures[r] <= temperatures[i]:
                    count += 1
                else:
                    result.append(count)
                    break

        result.append(0)
        return result