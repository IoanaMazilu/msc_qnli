speed_premise = 40
speed_hypothesis = 10

# the hypothesis refers to Bob's driving speed from City A to City B, also mentioned in the premise
if speed_premise!= speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speeds in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
