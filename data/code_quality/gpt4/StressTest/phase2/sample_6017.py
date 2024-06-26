baby_sitting_start_age_premise = 20
baby_sitting_start_age_hypothesis = 40

# The hypothesis talks about the age Jane started baby-sitting, which is referenced in the premise as well
if baby_sitting_start_age_hypothesis == baby_sitting_start_age_premise:
    # If the age in the hypothesis matches the age in the premise, we can infer entailment
    label = "entailment"
else:
    # If the age in the hypothesis does not match the age in the premise, we can infer contradiction
    label = "contradiction"

print(label)
