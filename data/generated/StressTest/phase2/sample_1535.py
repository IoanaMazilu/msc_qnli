# Premise: Tina has 12 shirts and 9 pants.
# Hypothesis: Tina has 32 shirts and 9 pants.
# Golden Label: contradiction

shirts_premise = 12
shirts_hypothesis = 32
pants_premise = 9
pants_hypothesis = 9

# the hypothesis refers to the number of shirts and pants Tina has, mentioned also in the premise
if shirts_premise != shirts_hypothesis:
    # check if the number of shirts in the hypothesis contradicts the number of shirts mentioned in the premise
    label = "contradiction"
elif pants_hypothesis != pants_premise:
    # check if the number of pants in the hypothesis contradicts the number of pants reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

