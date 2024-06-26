lime_picked_alyssa = 25.0
lime_picked_mike = 32.0
lime_picked_tom = 12.0
total_lime_picked = 61.0

# the hypothesis refers to the total number of limes picked, which is also mentioned in the premise
# compute the total number of limes picked in the premise
total_lime_picked_premise = lime_picked_alyssa + lime_picked_mike + lime_picked_tom
if total_lime_picked_premise!= total_lime_picked:
    # check if the total number of limes picked in the hypothesis contradicts the total number of limes picked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
