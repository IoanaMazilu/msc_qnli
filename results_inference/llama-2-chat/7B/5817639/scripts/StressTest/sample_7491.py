peanuts_premise = 4
peanuts_hypothesis = 1

# the hypothesis talks about the number of peanuts in a box, referenced also in the premise
if peanuts_hypothesis <= peanuts_premise:
    # check if the hypothesis value contradicts the estimate of 'peanuts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
