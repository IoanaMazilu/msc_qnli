# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for less than 4 years at 4% per annum simple interest?
# Golden Label: entailment

years_premise = 2
years_hypothesis = 4
interest_rate = 4

# the hypothesis talks about the term of a simple interest loan, which is also mentioned in the premise
if years_hypothesis < years_premise:
    # check if the hypothesized term contradicts the term in the premise
    label = "contradiction"
elif years_hypothesis == years_premise:
    # the term in the hypothesis is not less than the term in the premise, but it is exactly the same
    label = "contradiction"
else:
    # any term less than 'years_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

