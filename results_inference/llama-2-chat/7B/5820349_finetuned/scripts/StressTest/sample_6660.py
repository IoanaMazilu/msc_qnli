money_given_premise = 40
money_given_hypothesis = 70

# the hypothesis talks about the percentage of money Jones gave to his wife, also referenced in the premise
if money_given_hypothesis <= money_given_premise:
    # check if the hypothesis value contradicts the percentage of'money_given_premise'
    label = "contradiction"
else:
    # the premise gives a specific percentage of money given to the wife
    # any percentage less than'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
