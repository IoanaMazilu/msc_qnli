speed_premise = 30
speed_hypothesis = 20

# the hypothesis refers to the speed at which Cara drives
if speed_premise > speed_hypothesis:
    # the hypothesis contradicts the premise, as the premise states a higher speed
    label = "contradiction"
elif speed_hypothesis == 0:
    # the hypothesis is neutral, as it does not provide any information about the speed
    label = "neutral"
else:
    # the premise states a specific speed, and the hypothesis provides a lower speed
    # the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
