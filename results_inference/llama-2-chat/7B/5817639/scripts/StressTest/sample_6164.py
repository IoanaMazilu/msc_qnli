purchase_premise = 30
purchase_hypothesis = float(30) # handle the case where the hypothesis is a float value

# the hypothesis talks about the amount of wheat purchased, which is also mentioned in the premise
if purchase_hypothesis <= purchase_premise:
    # check if the hypothesis value contradicts the estimate of 'purchase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of wheat purchased
    # any amount of wheat greater than 'purchase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
