money_premise = 85
money_hypothesis = 95

# the hypothesis talks about the amount of money to be given, referenced also in the premise
if money_hypothesis <= money_premise:
    # check if the hypothesis value contradicts the estimate of more than'money_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money greater than'money_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
