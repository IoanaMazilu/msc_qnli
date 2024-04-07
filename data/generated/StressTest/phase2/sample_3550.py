# Premise: Bond (less than 8) wants to move from a point A to point D, but here 2 watchtowers (B & C) are present in the way of A to D.
# Hypothesis: Bond (007) wants to move from a point A to point D, but here 2 watchtowers (B & C) are present in the way of A to D.
# Golden Label: neutral

bond_number_premise = 8
bond_number_hypothesis = 7
watchtowers_premise = 2
watchtowers_hypothesis = 2

# the hypothesis talks about the number of Bond and the number of watchtowers, referenced also in the premise
if bond_number_hypothesis >= bond_number_premise:
    # check if the number of Bond in the hypothesis contradicts the estimate of less than 'bond_number_premise'
    label = "contradiction"
elif watchtowers_hypothesis != watchtowers_premise:
    # check if the number of watchtowers in the hypothesis contradicts the number of watchtowers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

