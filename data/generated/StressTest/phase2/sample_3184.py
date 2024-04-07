# Premise: Nitin borrowed some money at the rate of more than 2% p.
# Hypothesis: Nitin borrowed some money at the rate of 6% p.
# Golden Label: neutral

interest_rate_premise = 2
interest_rate_hypothesis = 6

# the hypothesis talks about the interest rate at which Nitin borrowed money, referenced also in the premise
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'interest_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the interest rate
    # any interest rate greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

