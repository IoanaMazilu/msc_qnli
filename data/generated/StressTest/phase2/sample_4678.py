# Premise: How much loss would Indu has suffered had she given it to Bindu for less than 4 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Golden Label: neutral

years_premise = 4
years_hypothesis = 2
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis refers to the number of years and the interest rate mentioned in the premise
if years_hypothesis > years_premise:
    # check if the number of 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

