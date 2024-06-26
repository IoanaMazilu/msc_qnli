gift_premise = 95
gift_hypothesis = float("less than 95")

# the hypothesis talks about the amount of money to be given, referenced also in the premise
if gift_hypothesis <= gift_premise:
    # check if the hypothesis value contradicts the estimate of 'gift_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money to be given
    # any amount of money greater than 'gift_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
