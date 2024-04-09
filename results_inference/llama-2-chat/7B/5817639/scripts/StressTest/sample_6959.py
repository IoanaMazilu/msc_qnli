toy_purchase_premise = 20
toy_purchase_hypothesis = 20
rate_premise = 375
rate_hypothesis = 675

# the hypothesis talks about the rate of toy purchase, which is also mentioned in the premise
if rate_hypothesis <= rate_premise:
    # check if the hypothesis rate contradicts the rate estimated in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of toy purchase
    # any rate greater than 'rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
