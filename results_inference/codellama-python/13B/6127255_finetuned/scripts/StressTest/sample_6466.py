peanuts_box_premise = 1
peanuts_added = 12
peanuts_box_hypothesis = 4

# the hypothesis talks about the number of peanuts in a box before and after Mary adds some, referenced also in the premise
if peanuts_box_hypothesis <= peanuts_box_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_box_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
