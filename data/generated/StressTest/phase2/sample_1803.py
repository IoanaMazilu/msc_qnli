# Premise: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of 8% p.
# Hypothesis: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of more than 5% p.
# Golden Label: entailment

interest_rate_premise = 8
interest_rate_hypothesis = 5

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis >= interest_rate_premise:
    # check if the estimate of 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

