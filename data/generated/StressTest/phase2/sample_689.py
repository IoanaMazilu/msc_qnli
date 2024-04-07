# Premise: Jane started baby-sitting when she was 18 years old.
# Hypothesis: Jane started baby-sitting when she was 78 years old.
# Golden Label: contradiction

babysitting_age_premise = 18
babysitting_age_hypothesis = 78

# the hypothesis refers to the age Jane started babysitting, mentioned also in the premise
if babysitting_age_hypothesis != babysitting_age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis and premise do not contradict, we can infer entailment
    label = "entailment"

print(label)

