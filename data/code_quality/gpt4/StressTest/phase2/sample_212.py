speed_premise = 60
speed_hypothesis = 20

# the hypothesis refers to the same driving speed from town A to town B as the premise
if speed_premise != speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)
