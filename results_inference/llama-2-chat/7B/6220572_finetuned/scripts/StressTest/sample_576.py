speed_premise = 40
speed_hypothesis = 70

# the hypothesis refers to the constant speed of Bob while driving from City A to City B
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the constant speed reported in the premise
    label = "contradiction"
else:
    # any speed less than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
