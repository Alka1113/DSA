class Solution(object):
    def angleClock(self, hour, minutes):
        hour_angle = (hour * 30) + (minutes * 0.5)
        minute_angle = minutes * 6

        angle = abs(hour_angle - minute_angle)

        if angle > 180:
            angle = 360 - angle

        return angle