speed_premise = 25
speed_hypothesis = 55

# the hypothesis refers to the speed of B starting from Mathura, also mentioned in the premise
if speed_hypothesis == speed_premise:
    # if the speed in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
else:
    # if the speed in the hypothesis is different than the one in the premise, we have a contradiction
    label = "contradiction"

print(label)
