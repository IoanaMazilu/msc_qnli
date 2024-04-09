boxes_sold_premise = 7
boxes_sold_hypothesis = 9

# the hypothesis talks about the number of boxes sold by Mark and Ann, referenced also in the premise
if boxes_sold_hypothesis <= boxes_sold_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boxes_sold_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of boxes sold by Mark and Ann
    # any number of boxes sold by Mark and Ann that is greater than or equal to the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
