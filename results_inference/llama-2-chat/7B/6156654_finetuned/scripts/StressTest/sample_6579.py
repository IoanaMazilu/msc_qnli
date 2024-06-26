sean_weight_premise = 200
total_weight_premise = 150 + 280
sean_weight_hypothesis = 800
total_weight_hypothesis = 150 + 280

# the hypothesis refers to Sean's weight and the total weight of packages in the elevator
if sean_weight_premise <= sean_weight_hypothesis:
    # check if Sean's weight in the premise contradicts the hypothesis of Sean weighing less than 800 pounds
    label = "contradiction"
elif total_weight_premise!= total_weight_hypothesis:
    # check if the total weight of packages in the premise contradicts the total weight of packages in the hypothesis
    label = "contradiction"
else:
    # if the premise and hypothesis values do not contradict, we can infer entailment
    label = "entailment"

print(label)
