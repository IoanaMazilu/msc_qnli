# Premise: How many years will it take John’s investment to double at a simple interest rate of 4% per annum.
# Hypothesis: How many years will it take John’s investment to double at a simple interest rate of more than 4% per annum.
# Golden Label: contradiction

interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis > interest_rate_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate_hypothesis < interest_rate_premise:
    # check if the hypothesis value is less than the premise value
    label = "contradiction"
else:
    # the hypothesis value and premise value are the same, which can infer entailment
    label = "entailment"

print(label)

