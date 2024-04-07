# Premise: Nitin borrowed some money at the rate of 6% p.
# Hypothesis: Nitin borrowed some money at the rate of 5% p.
# Golden Label: contradiction

interest_rate_premise = 6
interest_rate_hypothesis = 5

# the hypothesis talks about the interest rate of a loan, referenced also in the premise
if interest_rate_hypothesis == interest_rate_premise:
    # check if the interest rate in the hypothesis matches the interest rate in the premise
    label = "entailment"
else:
    # if the interest rates do not match, this is a contradiction
    label = "contradiction"

print(label)

