months_later_premise = 4
months_later_hypothesis = 4
investment_premise = 90000
investment_hypothesis = 90000

# the hypothesis refers to the number of months and the investment amount mentioned in the premise
if months_later_premise == months_later_hypothesis:
    # check if the estimate of 'investment_hypothesis' contradicts the investment amount in the premise
    if investment_hypothesis <= investment_premise:
        label = "contradiction"
    else:
        label = "entailment"
else:
    # the premise gives only an estimate for the number of months
    # any number of months greater than'months_later_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
