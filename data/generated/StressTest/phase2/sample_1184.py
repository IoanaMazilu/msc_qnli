# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for 5 years at 4% per annum simple interest?
# Golden Label: contradiction

years_premise = 2
years_hypothesis = 5
interest_rate = 4  # same interest rate in premise and hypothesis

# the hypothesis talks about the years of a simple interest calculation, referenced also in the premise
if years_hypothesis < years_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif years_hypothesis == years_premise:
    # if the hypothesis years equals the premise years, we can infer entailment
    label = "entailment"
else:
    # the premise gives a specific number of years for a simple interest calculation
    # any number of years greater than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

