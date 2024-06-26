money_to_give_premise = 85
money_to_give_hypothesis = 95

# the hypothesis talks about the amount of money given to John, referenced also in the premise
if money_to_give_hypothesis <= money_to_give_premise:
    # check if the hypothesis value contradicts the estimate of more than'money_to_give_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money
    # any amount of money greater than'money_to_give_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
#