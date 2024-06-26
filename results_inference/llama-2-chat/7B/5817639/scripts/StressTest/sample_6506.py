speed_premise = 40
speed_hypothesis = 10

# the hypothesis talks about a different constant speed than the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis speed contradicts the premise speed
    label = "contradiction"
else:
    # the premise provides a constant speed, while the hypothesis provides a different one
    # any speed greater than the premise speed is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
