speed_premise = 30
speed_hypothesis = 40

# the hypothesis refers to the speed of Cara's drive mentioned in the premise
if speed_premise != speed_hypothesis:
    # check if the speed mentioned in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speeds are equal, we can infer entailment
    label = "entailment"

print(label)
