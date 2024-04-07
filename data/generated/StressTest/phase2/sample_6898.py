# Premise: Mark sold more than 6 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold 7 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: neutral

boxes_sold_mark_premise = 6
boxes_sold_mark_hypothesis = 7
boxes_sold_ann_premise = 2
boxes_sold_ann_hypothesis = 2

# The hypothesis refers to the number of boxes sold by Mark and Ann, mentioned in the premise
if boxes_sold_mark_hypothesis <= boxes_sold_mark_premise:
    # check if the number of boxes sold by Mark in the hypothesis contradicts the estimate of more than 'boxes_sold_mark_premise'
    label = "contradiction"
elif boxes_sold_ann_hypothesis != boxes_sold_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann reported in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of boxes sold by Mark
    # any number of boxes greater than 'boxes_sold_mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

