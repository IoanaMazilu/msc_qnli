speed_premise = 40
speed_hypothesis = 70

# the hypothesis talks about the speed of driving from City A to City B, which is also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)