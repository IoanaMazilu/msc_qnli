percentage_given_premise = 70
percentage_given_hypothesis = 40

# the hypothesis talks about the percentage of money Jones gave to his wife, which is also referenced in the premise
if percentage_given_hypothesis >= percentage_given_premise:
    # check if the hypothesis value contradicts the estimate of less than 'percentage_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of money given
    # any percentage less than 'percentage_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
