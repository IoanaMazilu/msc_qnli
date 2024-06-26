gang_premise = 8
gang_hypothesis = 8

# the hypothesis refers to the number of gangs Andrew has, which is also mentioned in the premise
if gang_hypothesis >= gang_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
