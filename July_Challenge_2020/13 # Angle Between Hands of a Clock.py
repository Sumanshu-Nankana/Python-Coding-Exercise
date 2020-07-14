# Given two numbers, hour and minutes. 
# Return the smaller angle (in degrees) formed between the hour and the minute hand.

# Example 1:

# Input: hour = 12, minutes = 30
# Output: 165

# Example 2:

# Input: hour = 3, minutes = 30
# Output: 75

# Example 3:

# Input: hour = 3, minutes = 15
# Output: 7.5

# Example 4:

# Input: hour = 4, minutes = 50
# Output: 155

# Example 5:

# Input: hour = 12, minutes = 0
# Output: 0

# Constraints:
#     1 <= hour <= 12
#     0 <= minutes <= 59
#     Answers within 10^-5 of the actual value will be accepted as correct.

# ==========================================================================
# Accepted in Leetcode
#
# Approach - 
# Consider 12 as a Base
# find angle covered by minute hand by taking 12 as a reference
# find angle covered by hour hand by taking 12 as a reference
# Then subtract both
# if answer is > 180, then subtract from 360 (as we need to return smaller angle)
#
class Solution(object):
    def angleClock(self, hour, minutes):
       
        angle_made_by_hour_hand = (hour*30) + minutes*0.5
        angle_made_by_min_hand = minutes*6
        
        final_angle = abs(angle_made_by_hour_hand - angle_made_by_min_hand)
        if final_angle > 180: return 360-final_angle
        return final_angle

# ============================================================================
