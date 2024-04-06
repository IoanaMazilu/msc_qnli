# Premise: One in 10 babies (usually girls) will develop one.
# Hypothesis: One in 10 babies will develop a hemangioma.
# Golden Label: neutral

babies_premise = 0.1
babies_hypothesis = 0.1

# the hypothesis mentions the proportion of babies who will develop a hemangioma, which is also referenced in the premise
if babies_hypothesis != babies_premise:
    # check if the proportion of babies in the hypothesis contradicts the proportion of babies in the premise
    label = "contradiction"
else:
    # if the proportion of babies in the hypothesis does not contradict the proportion of babies in the premise, we can infer entailment
    label = "entailment"

print(label)

