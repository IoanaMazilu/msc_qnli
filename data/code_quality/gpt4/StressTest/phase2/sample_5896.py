speed_premise = 30
speed_hypothesis = 20

# The hypothesis refers to the speed of A mentioned in the premise
if speed_hypothesis >= speed_premise:
    # Check if the speed in the hypothesis contradicts the premise estimate of less than 'speed_premise'
    label = "contradiction"
else:
    # Any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
