boxes_mark_premise = 1
boxes_mark_hypothesis = 6
boxes_ann_premise = 2
boxes_ann_hypothesis = 2

# the hypothesis refers to the number of boxes sold by Mark and Ann as mentioned in the premise
if boxes_mark_hypothesis <= boxes_mark_premise:
    # check if the hypothesis value contradicts the estimate of 'boxes_mark_premise'
    label = "contradiction"
elif boxes_ann_hypothesis != boxes_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes sold by Mark
    # any number of boxes more than 'boxes_mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
