total_pens_premise = 12
total_pens_hypothesis = 12

# the hypothesis refers to the total number of pens purchased and the premise mentions the total cost
if total_pens_hypothesis <= total_pens_premise:
    # check if the estimate of 'total_pens_hypothesis' contradicts the total number of pens in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of pens
    # any number of pens greater than 'total_pens_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
