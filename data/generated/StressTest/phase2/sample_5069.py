# Premise: Quarters (US $0.25) are stacked in 18 columns.
# Hypothesis: Quarters (US $0.25) are stacked in 38 columns.
# Golden Label: contradiction

columns_premise = 18
columns_hypothesis = 38

# the hypothesis talks about the number of columns of quarters, referenced also in the premise
if columns_hypothesis != columns_premise:
    # check if the number of columns in the hypothesis contradicts the number of columns reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

