# Premise: Jane started baby-sitting when she was 16 years old.
# Hypothesis: Jane started baby-sitting when she was 36 years old.
# Golden Label: contradiction

start_age_premise = 16
start_age_hypothesis = 36

# the hypothesis refers to the age Jane started baby-sitting, mentioned in the premise
if start_age_premise != start_age_hypothesis:
    # check if the age in the hypothesis contradicts the age stated in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age stated in the premise, we can infer entailment
    label = "entailment"

print(label)

