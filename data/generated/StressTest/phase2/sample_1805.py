# Premise: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of 8% p.
# Hypothesis: The compound interest earned by Sunil on a certain amount at the end of two years at the rate of 4% p.
# Golden Label: contradiction

interest_rate_premise = 8
interest_rate_hypothesis = 4

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_premise != interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the interest rate in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)

