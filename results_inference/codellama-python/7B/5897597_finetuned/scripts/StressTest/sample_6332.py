cigarettes_per_box_premise = 5
cigarettes_per_box_hypothesis = 1
packing_time_premise = 2
packing_time_hypothesis = 2

# the hypothesis refers to the number of cigarettes per box and the packing time mentioned in the premise
if cigarettes_per_box_premise!= cigarettes_per_box_hypothesis:
    # check if the number of cigarettes per box in the hypothesis contradicts the number of cigarettes per box in the premise
    label = "contradiction"
elif packing_time_premise!= packing_time_hypothesis:
    # check if the packing time in the hypothesis contradicts the packing time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
