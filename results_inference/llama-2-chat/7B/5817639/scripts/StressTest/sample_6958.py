toy_purchases_premise = 20
toy_purchases_hypothesis = 375

# the hypothesis talks about the rate at which toys were purchased, referenced also in the premise
if toy_purchases_hypothesis <= toy_purchases_premise:
    # check if the hypothesis value contradicts the estimate of more than 'toy_purchases_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of toy purchases
    # any rate of toy purchases greater than 'toy_purchases_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
