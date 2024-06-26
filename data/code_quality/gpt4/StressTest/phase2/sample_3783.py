mark_boxes_premise = 9
mark_boxes_hypothesis = 5
ann_boxes_premise = 2
ann_boxes_hypothesis = 2

# the hypothesis talks about the number of boxes sold by Mark and Ann, referenced also in the premise
if mark_boxes_hypothesis < mark_boxes_premise:
    # check if the hypothesis estimate contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
elif ann_boxes_hypothesis != ann_boxes_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
