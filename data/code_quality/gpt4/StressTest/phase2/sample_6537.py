speed_premise = 30
speed_hypothesis = 50

# the hypothesis talks about the speed Cara drives at, which is also mentioned in the premise
if speed_premise >= speed_hypothesis:
    # check if the speed in the premise contradicts the estimate of less than 'speed_hypothesis'
    label = "contradiction"
else:
    # the premise provides a specific number for the speed
    # any speed less than 'speed_hypothesis' is consistent with the premise, but 30 miles per hour can be explicitly entailed from the premise
    label = "entailment"

print(label)
