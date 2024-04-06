# Premise: U.S. public pension gap at least $2 trillion.
# Hypothesis: US public pension gap at least $2 trillion: Moody's.
# Golden Label: entailment

pension_gap_premise = 2e12 # in dollars
pension_gap_hypothesis = 2e12 # in dollars

# the hypothesis and premise mention the US public pension gap
if pension_gap_hypothesis != pension_gap_premise:
    # check if the pension gap in the hypothesis contradicts the pension gap in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

