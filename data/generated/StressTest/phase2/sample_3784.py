# Premise: Mark sold more than 5 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold 9 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: neutral

boxes_mark_premise = 5
boxes_mark_hypothesis = 9
boxes_ann_premise = 2
boxes_ann_hypothesis = 2

# the hypothesis talks about the number of boxes sold by Mark and Ann, referenced also in the premise
if boxes_mark_hypothesis <= boxes_mark_premise:
    # check if the hypothesis value contradicts the estimate of more than 'boxes_mark_premise'
    label = "contradiction"
elif boxes_ann_hypothesis != boxes_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes sold by Mark
    # any number of boxes greater than 'boxes_mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
