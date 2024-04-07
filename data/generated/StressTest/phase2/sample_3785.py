# Premise: Mark sold 9 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold less than 9 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: contradiction

mark_boxes_premise = 9
mark_boxes_hypothesis = 9
ann_boxes_premise = 2
ann_boxes_hypothesis = 2

# the hypothesis refers to the number of boxes sold by Mark and Ann mentioned in the premise
if mark_boxes_hypothesis < mark_boxes_premise:
    # check if the estimate of 'mark_boxes_hypothesis' contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
elif ann_boxes_hypothesis != ann_boxes_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
