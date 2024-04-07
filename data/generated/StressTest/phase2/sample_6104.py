# Premise: Jane started baby-sitting when she was 18 years old.
# Hypothesis: Jane started baby-sitting when she was 58 years old.
# Golden Label: contradiction

baby_sitting_start_age_premise = 18
baby_sitting_start_age_hypothesis = 58

# the hypothesis refers to the age Jane started baby-sitting, mentioned in the premise
if baby_sitting_start_age_hypothesis != baby_sitting_start_age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis age does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

