speed_premise = 60
speed_hypothesis = 30

# check if the hypothesis speed is less than the premise speed
if speed_hypothesis < speed_premise:
    # the hypothesis speed contradicts the premise speed
    label = "contradiction"
else:
    # the premise speed is greater than the hypothesis speed, so the hypothesis cannot be entailed from the premise
    label = "neutral"

print(label)
