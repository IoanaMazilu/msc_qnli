boxes_sold_premise = 1
boxes_sold_hypothesis = 6

# the hypothesis talks about the number of boxes sold by Mark and Ann, referenced also in the premise
if boxes_sold_hypothesis <= boxes_sold_premise:
    # check if the hypothesis value contradicts the estimate of more than 'boxes_sold_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes sold by Mark and Ann
    # any number of boxes sold by Mark and Ann greater than 'boxes_sold_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
