mark_boxes_premise = n - 1
ann_boxes_premise = n - 2
mark_boxes_hypothesis = 6 + (n - 1)
ann_boxes_hypothesis = 2 + (n - 1)

# the hypothesis refers to the number of boxes sold by Mark and Ann, mentioned in the premise
if mark_boxes_premise <= mark_boxes_hypothesis and ann_boxes_premise <= ann_boxes_hypothesis:
    # check if the estimates of Mark and Ann's box sales in the hypothesis contradict the premise
    label = "contradiction"
elif mark_boxes_hypothesis!= (n - 1) or ann_boxes_hypothesis!= (n - 2):
    # check if the number of boxes sold by Mark and Ann in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
