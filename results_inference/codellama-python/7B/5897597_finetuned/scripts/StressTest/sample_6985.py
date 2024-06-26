pens_purchased_premise = 22
pens_purchased_hypothesis = 12

# the hypothesis refers to the number of pens purchased by Elena, which is also mentioned in the premise
if pens_purchased_hypothesis >= pens_purchased_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pens_purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pens
    # any number of pens less than 'pens_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
