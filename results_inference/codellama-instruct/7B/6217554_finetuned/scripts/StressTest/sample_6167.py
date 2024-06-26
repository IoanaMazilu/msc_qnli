money_given_premise = 95
money_given_hypothesis = 95

if money_given_hypothesis >= money_given_premise:
    # check if the hypothesis value contradicts the exact amount of money given in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of money
    # any amount of money less than'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
