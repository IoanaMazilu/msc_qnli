# Premise: How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?
# Hypothesis: How much loss would Indu has suffered had she given it to Bindu for 7 years at 4% per annum simple interest?
# Golden Label: contradiction

years_premise = 2
years_hypothesis = 7
interest_rate = 4

# the hypothesis refers to the number of years mentioned in the premise
if years_premise == years_hypothesis:
    # if the number of years in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"
elif years_premise != years_hypothesis:
    # if the number of years in the hypothesis is different from the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the number of years in the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise, we can infer neutrality
    label = "neutral"

print(label)

