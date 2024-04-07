# Premise: Nitin borrowed some money at the rate of less than 7% p.
# Hypothesis: Nitin borrowed some money at the rate of 6% p.
# Golden Label: neutral

interest_rate_premise = 7
interest_rate_hypothesis = 6

# the hypothesis refers to the interest rate of a loan mentioned in the premise
if interest_rate_hypothesis >= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the estimate of less than 'interest_rate_premise'
    label = "contradiction"
else:
    # if the interest rate in the hypothesis is less than the 'interest_rate_premise', it's consistent with the premise
    # but we cannot explicitly entail it from the premise
    label = "neutral"

print(label)

