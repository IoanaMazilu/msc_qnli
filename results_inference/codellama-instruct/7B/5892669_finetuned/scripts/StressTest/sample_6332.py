cigarettes_per_box_premise = 5
cigarettes_per_box_hypothesis = 1

# the hypothesis refers to the number of cigarettes per box mentioned in the premise
if cigarettes_per_box_hypothesis!= cigarettes_per_box_premise:
    # check if the number of cigarettes per box in the hypothesis contradicts the number of cigarettes per box reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
