money_given_percentage_premise = 10
money_given_percentage_hypothesis = 40

# The hypothesis refers to the percentage of money Jones gave to his wife, which is also mentioned in the premise.
if money_given_percentage_hypothesis <= money_given_percentage_premise:
    # Check if the percentage in the hypothesis contradicts the estimate of more than 'money_given_percentage_premise'.
    label = "contradiction"
else:
    # The premise gives only an estimate for the percentage of money given.
    # Any percentage greater than 'money_given_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)
