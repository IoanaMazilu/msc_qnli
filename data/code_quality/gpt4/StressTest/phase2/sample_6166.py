money_to_give_premise = 85
money_to_give_hypothesis = 95

# the hypothesis refers to the amount of money I want to give to John, mentioned also in the premise
if money_to_give_hypothesis <= money_to_give_premise:
    # check if the amount of money in the hypothesis contradicts the premise's estimate of more than 'money_to_give_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the money I want to give to John
    # any amount greater than 'money_to_give_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
