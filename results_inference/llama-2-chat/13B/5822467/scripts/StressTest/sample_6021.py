borrowed_premise = 5000
borrowed_hypothesis = 2000

# the hypothesis refers to the amount of money borrowed for college education
if borrowed_hypothesis > borrowed_premise:
    # the hypothesis contradicts the premise, as the estimated amount borrowed is higher than the amount reported in the premise
    label = "contradiction"
elif borrowed_hypothesis == borrowed_premise:
    # the hypothesis and premise have the same value, so there is no contradiction or entailment
    label = "neutral"
else:
    # the premise reports a specific amount borrowed, and the hypothesis gives a more general estimate
    # any amount borrowed greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
