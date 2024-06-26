speed_premise = 40
speed_hypothesis = 10

# the hypothesis refers to the speed of Bob's driving from City A to City B, mentioned in the premise
if speed_premise!= speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the speed in the premise, we can infer entailment
    label = "entailment"

print(label)
