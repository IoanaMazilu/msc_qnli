speed_premise = 45
speed_hypothesis = 65

# the hypothesis talks about the speed of Venki's driving, also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)
