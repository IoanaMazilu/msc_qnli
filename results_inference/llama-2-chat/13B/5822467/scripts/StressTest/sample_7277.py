molly_max_speed_premise = 100
molly_max_speed_hypothesis = 50

# the hypothesis refers to the rate of driving, which is a numerical value
if molly_max_speed_premise > molly_max_speed_hypothesis:
    # the hypothesis contradicts the premise, as the estimated speed is lower than the premise
    label = "contradiction"
elif molly_max_speed_hypothesis == 0:
    # the hypothesis does not provide any information about the speed, so the premise is neutral
    label = "neutral"
else:
    # the premise and hypothesis values are consistent, but the hypothesis does not explicitly entail the premise
    label = "entailment"

print(label)
