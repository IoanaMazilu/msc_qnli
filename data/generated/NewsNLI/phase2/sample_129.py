# Premise: Of the 30 Americans killed in the helicopter crash, 17 were Navy SEALs.
# Hypothesis: 30 U.S. personnel were killed in the attack.
# Golden Label: neutral

americans_killed_premise = 30
americans_killed_hypothesis = 30

# the hypothesis mentions the total number of U.S. personnel killed, which is also mentioned in the premise
if americans_killed_hypothesis != americans_killed_premise:
    # check if the number of U.S. personnel killed in the hypothesis contradicts the number of Americans killed reported in the premise
    label = "contradiction"
else:
    # if the number of U.S. personnel killed in the hypothesis does not contradict the number of Americans killed in the premise, we can infer entailment
    label = "entailment"

print(label)

