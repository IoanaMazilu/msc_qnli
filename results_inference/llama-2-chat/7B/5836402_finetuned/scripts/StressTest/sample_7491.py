peanuts_in_box_premise = 4
peanuts_in_box_hypothesis = 1

# the hypothesis refers to the number of peanuts in a box, which is also mentioned in the premise
if peanuts_in_box_hypothesis <= peanuts_in_box_premise:
    # check if the hypothesis value contradicts the estimate of 'peanuts_in_box_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_in_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
