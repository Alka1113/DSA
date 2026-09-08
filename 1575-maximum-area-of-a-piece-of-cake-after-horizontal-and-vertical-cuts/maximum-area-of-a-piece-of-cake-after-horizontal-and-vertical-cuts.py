class Solution:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts.sort()
        verticalCuts.sort()

        max_h = horizontalCuts[0]
        max_w = verticalCuts[0]

        # Find largest gap between horizontal cuts
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])

        # Gap from last horizontal cut to bottom
        max_h = max(max_h, h - horizontalCuts[-1])

        # Find largest gap between vertical cuts
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1])

        # Gap from last vertical cut to right
        max_w = max(max_w, w - verticalCuts[-1])

        return (max_h * max_w) % (10**9 + 7)