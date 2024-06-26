boxes_sold_premise = 6
boxes_sold_hypothesis = 1

# the hypothesis refers to the number of boxes sold by Mark and Ann, mentioned in the premise
if boxes_sold_premise <= boxes_sold_hypothesis:
    # check if the estimate of 'boxes_sold_hypothesis' contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boxes sold by Mark and Ann
    # any number of boxes sold by Mark greater than 'boxes_sold_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
