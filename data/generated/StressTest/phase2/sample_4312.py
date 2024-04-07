# Premise: Mark sold more than 1 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold 8 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: neutral

boxes_sold_mark_premise = 1
boxes_sold_mark_hypothesis = 8
boxes_sold_ann_premise = 2
boxes_sold_ann_hypothesis = 2

# the hypothesis refers to the number of boxes both Mark and Ann sold, which is also mentioned in the premise
if boxes_sold_mark_hypothesis <= boxes_sold_mark_premise:
    # check if the number of boxes sold by Mark in the hypothesis contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
elif boxes_sold_ann_hypothesis != boxes_sold_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann in the premise
    label = "contradiction"
else:
    # any number of boxes sold by Mark greater than 'boxes_sold_mark_premise' and equal to 'boxes_sold_ann_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

