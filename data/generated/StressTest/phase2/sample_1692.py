# Premise: Jane started baby-sitting when she was 16 years old.
# Hypothesis: Jane started baby-sitting when she was less than 86 years old.
# Golden Label: entailment

babysitting_start_age_premise = 16
babysitting_start_age_hypothesis = 86

# the hypothesis refers to the age Jane started babysitting that was mentioned in the premise
if babysitting_start_age_hypothesis < babysitting_start_age_premise:
    # check if the age in the hypothesis contradicts the age when Jane started babysitting in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis is greater than or equal to the age in the premise, we can infer entailment
    label = "entailment"

print(label)

