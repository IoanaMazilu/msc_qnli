peak_height_premise = 10197 # feet
distance_premise = 100 # miles

peak_height_hypothesis = None # The hypothesis does not mention the height of the peak
distance_hypothesis = 100 # miles

# The hypothesis mentions the distance from Anchorage, which is also referenced in the premise
# However, the hypothesis does not mention the height of the peak, which cannot be entailed from the premise

if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance does not contradict the premise, but the height of the peak is not mentioned in the hypothesis, we have a neutral situation
    label = "neutral"

print(label)
