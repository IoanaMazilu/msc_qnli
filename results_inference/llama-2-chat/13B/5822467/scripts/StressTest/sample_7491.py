peanuts_premise = 4
more_peanuts_hypothesis = 1

# the hypothesis refers to the number of peanuts in the box
if more_peanuts_hypothesis <= peanuts_premise:
    # check if the estimate of'more_peanuts_hypothesis' contradicts the number of peanuts in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
