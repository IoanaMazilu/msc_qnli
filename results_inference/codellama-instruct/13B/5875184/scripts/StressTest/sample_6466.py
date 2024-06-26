peanuts_box_premise = 1
peanuts_box_hypothesis = 4

# the hypothesis refers to the number of peanuts in a box mentioned in the premise
if peanuts_box_premise <= peanuts_box_hypothesis:
    # check if the estimate of 'peanuts_box_hypothesis' contradicts the number of peanuts in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
