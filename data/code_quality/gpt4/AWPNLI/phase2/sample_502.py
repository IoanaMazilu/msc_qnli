bottle_caps_per_box_premise = 35.0
num_boxes_premise = 7.0
total_bottle_caps_hypothesis = 245.0

# the hypothesis refers to the total number of bottle caps, which are also mentioned in the premise
# compute the total number of bottle caps in the premise
total_bottle_caps_premise = bottle_caps_per_box_premise * num_boxes_premise
if total_bottle_caps_hypothesis != total_bottle_caps_premise:
    # check if the total number of bottle caps in the hypothesis contradicts the total number of bottle caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
