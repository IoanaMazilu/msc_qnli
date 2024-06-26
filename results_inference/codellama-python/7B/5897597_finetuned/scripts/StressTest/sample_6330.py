cigarettes_boxes_premise = 5
cigarettes_boxes_hypothesis = 8

# the hypothesis refers to the number of boxes of cigarettes in a case mentioned in the premise
if cigarettes_boxes_premise >= cigarettes_boxes_hypothesis:
    # check if the number of boxes of cigarettes in the premise contradicts the estimate of less than 'cigarettes_boxes_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
