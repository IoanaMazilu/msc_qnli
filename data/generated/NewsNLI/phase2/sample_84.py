# Premise: Texan Gregory Rose, who's uninsured, was diagnosed with leukemia at 23.
# Hypothesis: He had leukemia, at 23.
# Golden Label: entailment

age_diagnosed_premise = 23
age_diagnosed_hypothesis = 23

# the hypothesis mentions the age at which the person was diagnosed with leukemia, which is also mentioned in the premise
if age_diagnosed_hypothesis != age_diagnosed_premise:
    # check if the age at diagnosis in the hypothesis contradicts the age at diagnosis reported in the premise
    label = "contradiction"
else:
    # if the age at diagnosis in the hypothesis does not contradict the age at diagnosis in the premise, we can infer entailment
    label = "entailment"

print(label)

