speed_premise = 20
speed_hypothesis = 30

# the hypothesis refers to the speed of Ed's driving, which is also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict it
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
