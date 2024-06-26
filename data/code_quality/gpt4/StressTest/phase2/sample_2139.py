speed_premise = 40
speed_hypothesis = 80

# the hypothesis refers to the speed of Bob's driving from City A to City B, mentioned also in the premise
if speed_premise > speed_hypothesis:
    # check if the driving speed in the premise contradicts the estimate of 'speed_hypothesis'
    label = "contradiction"
elif speed_premise != speed_hypothesis:
    # the premise gives an exact speed for Bob's drive
    # any speed less than 'speed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
