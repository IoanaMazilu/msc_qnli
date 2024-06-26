pencil_boxes_premise = 4.0
pencils_per_box_premise = 648.0
total_pencils_hypothesis = 2595.0

# the hypothesis refers to the total number of pencils, which is derived from the premise
# compute the total number of pencils in the premise
total_pencils_premise = pencil_boxes_premise * pencils_per_box_premise
if total_pencils_hypothesis != total_pencils_premise:
    # check if the total number of pencils in the hypothesis contradicts the total number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
