mark_boxes_hypothesis = 7
mark_boxes_premise = 6
ann_boxes_hypothesis = 2
ann_boxes_premise = 2

# the hypothesis talks about the number of boxes sold by Mark and Ann, referenced also in the premise
if mark_boxes_hypothesis <= mark_boxes_premise:
    # check if the hypothesis value contradicts the estimate of more than'mark_boxes_premise'
    label = "contradiction"
elif ann_boxes_hypothesis!= ann_boxes_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes sold by Mark
    # any number of boxes sold by Mark greater than'mark_boxes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
