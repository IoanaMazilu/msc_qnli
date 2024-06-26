total_pens_premise = 12
total_pens_hypothesis = 12

# the hypothesis refers to the total number of pens purchased by Elena, mentioned in the premise
if total_pens_hypothesis <= total_pens_premise:
    # check if the hypothesis value contradicts the exact number of 'total_pens_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of pens purchased
    # any number of pens greater than 'total_pens_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
