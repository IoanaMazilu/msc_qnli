speed_premise = 50
speed_hypothesis = 30

# the hypothesis refers to the speed at which Cara drives
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif speed_premise > speed_hypothesis:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the speed
    # any speed less than 50 miles per hour is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
