money_given_premise = 85
money_given_hypothesis = 95

# the hypothesis talks about the amount of money given to John, referenced also in the premise
if money_given_hypothesis <= money_given_premise:
    # check if the hypothesis value contradicts the estimate of more than'money_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money greater than'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
