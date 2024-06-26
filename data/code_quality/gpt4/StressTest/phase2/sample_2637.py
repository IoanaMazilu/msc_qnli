additional_boxes_premise = 2
additional_boxes_hypothesis = 5

# the hypothesis refers to the number of additional boxes mentioned in the premise
if additional_boxes_hypothesis <= additional_boxes_premise:
    # check if the estimate of 'additional_boxes_hypothesis' contradicts the number of additional boxes in the premise
    label = "contradiction"
elif additional_boxes_hypothesis != additional_boxes_premise:
    # check if the number of additional boxes in the hypothesis contradicts the number of additional boxes reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
