# Premise: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of more than 7% p.
# Hypothesis: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of 8% p.
# Golden Label: neutral

interest_rate_premise = 7
interest_rate_hypothesis = 8

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'interest_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the interest rate
    # any interest rate greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

