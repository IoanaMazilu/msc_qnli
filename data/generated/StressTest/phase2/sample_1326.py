# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for less than 8 years at 4% per annum simple interest?
# Golden Label: entailment

years_premise = 2
years_hypothesis = 8
interest_rate = 4

# the hypothesis talks about the number of years and interest rate in a context similar to the premise
if years_hypothesis <= years_premise:
    # check if the years value in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
elif interest_rate != 4:
    # check if the interest rate in the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of years and interest rate
    # any number of years less than 'years_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

