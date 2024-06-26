gift_to_john_premise = 85
gift_to_john_hypothesis = 95

# the hypothesis talks about the amount of money to be given to John, referenced also in the premise
if gift_to_john_hypothesis <= gift_to_john_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gift_to_john_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money greater than 'gift_to_john_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
