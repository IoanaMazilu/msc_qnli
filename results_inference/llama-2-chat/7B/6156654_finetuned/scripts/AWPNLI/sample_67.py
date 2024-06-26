lime_picked_alyssa = 25.0
lime_picked_mike = 32.0
lime_picked_tom = 12.0
total_lime_picked = lime_picked_alyssa + lime_picked_mike + lime_picked_tom

# the hypothesis refers to the total number of limes picked, which can be calculated from the premise
if total_lime_picked == 61.0:
    # if the hypothesis value and the calculated value are equal, it is an entailment
    label = "entailment"
else:
    # if the hypothesis value does not match the calculated value, it is a contradiction
    label = "contradiction"

print(label)
