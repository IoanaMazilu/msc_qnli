# Premise: If side AC = 20 units, what is the area of the triangle?
# Hypothesis: If side AC = more than 20 units, what is the area of the triangle?
# Golden Label: contradiction

side_ac_premise = 20
side_ac_hypothesis = 20

# the hypothesis refers to the length of side AC mentioned in the premise
if side_ac_hypothesis > side_ac_premise:
    # checks if the length of side AC in the hypothesis contradicts the length given in the premise
    label = "contradiction"
else:
    # if the length of side AC in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

