money_given_premise = 60
money_given_hypothesis = 40

# the hypothesis refers to the percentage of money given by Jones to his wife
if money_given_hypothesis >= money_given_premise:
    # check if the hypothesis value contradicts the estimate of less than'money_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of money given by Jones to his wife
    # any percentage of money given by Jones to his wife less than'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
