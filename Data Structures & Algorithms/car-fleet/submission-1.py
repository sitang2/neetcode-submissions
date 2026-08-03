class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Array 1 = position
        # Array 2 = speed
        # Position[i] = ith car
        # Speed[i] = speed of ith car
        # Target = destination (miles)

        pairs = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)