money_given_percentage_premise = 60
money_given_percentage_hypothesis = 40

# the hypothesis talks about the percentage of money Jones gave to his wife, referenced also in the premise
if money_given_percentage_hypothesis >= money_given_percentage_premise:
    # check if the hypothesis value contradicts the estimate of less than'money_given_percentage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of money given
    # any percentage of money less than'money_given_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
