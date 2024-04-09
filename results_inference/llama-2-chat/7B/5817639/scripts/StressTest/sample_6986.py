pen_purchase_premise = 12
pen_purchase_hypothesis = 12

# the hypothesis talks about the number of pens purchased by Elena, referenced also in the premise
if pen_purchase_hypothesis <= pen_purchase_premise:
    # check if the hypothesis value contradicts the estimate of 'pen_purchase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pens purchased
    # any number of pens greater than 'pen_purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
