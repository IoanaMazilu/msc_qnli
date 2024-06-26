money_given_premise = 40
money_given_hypothesis = 60

# the hypothesis talks about the percentage of money given by Jones, also referenced in the premise
if money_given_hypothesis >= money_given_premise:
    # check if the estimate of'money_given_hypothesis' contradicts the percentage of money given in the premise
    label = "contradiction"
else:
    # any percentage of money less than'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
