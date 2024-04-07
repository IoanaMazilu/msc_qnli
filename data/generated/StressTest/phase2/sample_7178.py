# Premise: 4800 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: more than 4800 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: contradiction

total_share_premise = 4800
total_share_hypothesis = 4800

# the hypothesis and premise both talk about the total share among John, Jose & Binoy
if total_share_hypothesis <= total_share_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

