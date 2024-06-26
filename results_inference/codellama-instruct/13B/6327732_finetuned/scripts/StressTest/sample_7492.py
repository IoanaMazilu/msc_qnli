peanuts_box_premise = 1
peanuts_box_hypothesis = 4

# the hypothesis refers to the number of peanuts in a box, which is also mentioned in the premise
if peanuts_box_premise <= peanuts_box_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_box_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
