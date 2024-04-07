# Premise: Nitin borrowed some money at the rate of 6% p.
# Hypothesis: Nitin borrowed some money at the rate of less than 7% p.
# Golden Label: entailment

interest_rate_premise = 6
interest_rate_hypothesis = 7

# the hypothesis refers to the interest rate for money borrowed by Nitin, mentioned in the premise
if interest_rate_premise >= interest_rate_hypothesis:
    # check if the interest rate in the premise contradicts the estimate of less than 'interest_rate_hypothesis'
    label = "contradiction"
else:
    # if the interest rate in the premise does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

