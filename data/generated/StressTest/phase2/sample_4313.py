# Premise: Mark sold 8 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold 5 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: contradiction

mark_boxes_sold_premise = 8
mark_boxes_sold_hypothesis = 5
ann_boxes_sold_premise = 2
ann_boxes_sold_hypothesis = 2

# the hypothesis refers to the number of boxes sold by Mark and Ann, as mentioned in the premise
if mark_boxes_sold_hypothesis != mark_boxes_sold_premise:
    # check if the number of boxes sold by Mark in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
elif ann_boxes_sold_hypothesis != ann_boxes_sold_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
else:
    # if the numbers in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

