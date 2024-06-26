speed_premise = 37
speed_hypothesis = 57

# the hypothesis talks about Glen's driving speed, also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speeds are the same, we can infer entailment
    label = "entailment"

print(label)
