# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for 6 years at 4% per annum simple interest?
# Golden Label: contradiction

years_premise = 2
years_hypothesis = 6
interest_rate = 4  # this value is the same in both premise and hypothesis

# the hypothesis refers to a scenario described in the premise but changes the number of years
if years_hypothesis < years_premise:
    # check if the number of years in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
elif years_hypothesis == years_premise:
    # if the number of years in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"
else:
    # if the number of years in the hypothesis is greater than in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

