purchased_premise = 20
purchased_hypothesis = 60

# the hypothesis talks about the number of items purchased, which is also referenced in the premise
if purchased_hypothesis <= purchased_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of items purchased
    # any number of items purchased greater than 'purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
