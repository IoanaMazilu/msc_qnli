# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for less than 2 years at 4% per annum simple interest?
# Golden Label: contradiction

years_premise = 2
years_hypothesis = 2
interest_rate = 4

# the hypothesis refers to the number of years and the interest rate mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the 'years_hypothesis' contradicts the time period mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years less than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
