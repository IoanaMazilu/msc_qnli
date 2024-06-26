money_fraction_premise = 4/12
money_fraction_hypothesis = 7/12

# the hypothesis refers to a fraction of a sum of money mentioned in the premise
if money_fraction_hypothesis <= money_fraction_premise:
    # check if the hypothesis fraction contradicts the estimate of more than 'money_fraction_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the fraction of the sum of money
    # any fraction greater than 'money_fraction_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
