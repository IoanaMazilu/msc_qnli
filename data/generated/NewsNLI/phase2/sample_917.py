# Premise: Underworld Awakening -- $25.4 million.
# Hypothesis: '' Underworld Awakening'' debuted in first place with $25.4 million.
# Golden Label: neutral

earnings_premise = 25.4
earnings_hypothesis = 25.4

# the hypothesis mentions the earnings of the movie which is also mentioned in the premise
if earnings_hypothesis != earnings_premise:
    # check if the earnings in the hypothesis contradicts the earnings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

