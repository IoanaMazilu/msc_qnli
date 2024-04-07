# Premise: Mark sold less than 81 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold 11 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: neutral

mark_boxes_sold_premise = 81
mark_boxes_sold_hypothesis = 11
ann_boxes_sold_premise = 2
ann_boxes_sold_hypothesis = 2

# the hypothesis refers to the number of boxes sold by Mark and Ann, which is also mentioned in the premise
if mark_boxes_sold_hypothesis >= mark_boxes_sold_premise:
    # check if the number of boxes Mark sold in the hypothesis contradicts the estimate of less than 'mark_boxes_sold_premise'
    label = "contradiction"
elif ann_boxes_sold_hypothesis != ann_boxes_sold_premise:
    # check if the number of boxes Ann sold in the hypothesis contradicts the number of boxes Ann sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

