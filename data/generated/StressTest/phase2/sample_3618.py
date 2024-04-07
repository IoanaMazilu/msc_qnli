# Premise: Mark sold 11 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold less than 81 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: entailment

mark_boxes_premise = 11
mark_boxes_hypothesis = 81
ann_boxes_premise = 2
ann_boxes_hypothesis = 2

# the hypothesis refers to the number of boxes Mark and Ann sold, mentioned in the premise
if mark_boxes_hypothesis < mark_boxes_premise:
    # check if the estimate of 'mark_boxes_hypothesis' contradicts the number of boxes Mark sold in the premise
    label = "contradiction"
elif ann_boxes_hypothesis != ann_boxes_premise:
    # check if the number of boxes Ann sold in the hypothesis contradicts the number of boxes Ann sold in the premise
    label = "contradiction"
elif mark_boxes_hypothesis == mark_boxes_premise:
    # if the hypothesis values equal the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis estimates do not contradict the premise ones and are not equal, we can infer neutrality
    label = "neutral"

print(label)

