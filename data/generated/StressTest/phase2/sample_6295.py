# Premise: Jones gave less than 60% of the money he had to his wife.
# Hypothesis: Jones gave 40% of the money he had to his wife.
# Golden Label: neutral

money_given_premise = 60
money_given_hypothesis = 40

# the hypothesis talks about the percentage of money Jones gave to his wife, which is also mentioned in the premise
if money_given_hypothesis >= money_given_premise:
    # check if the hypothesis value contradicts the estimate of less than 'money_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of money given
    # any percentage less than 'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

