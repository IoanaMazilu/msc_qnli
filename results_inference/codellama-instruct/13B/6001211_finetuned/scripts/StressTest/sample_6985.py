total_pens_premise = 22
total_pens_hypothesis = 12

# the hypothesis refers to the total number of pens purchased by Elena, which is also mentioned in the premise
if total_pens_hypothesis >= total_pens_premise:
    # check if the total number of pens in the hypothesis contradicts the estimate of less than 'total_pens_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of pens
    # any number of pens less than 'total_pens_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
