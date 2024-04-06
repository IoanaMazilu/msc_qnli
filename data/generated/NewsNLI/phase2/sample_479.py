# Premise: By 18, he'd lost all the hair on his head and body.
# Hypothesis: Rhodes lost all the hair on his head and body by 18.
# Golden Label: entailment

age_premise = 18
age_hypothesis = 18

# the hypothesis mentions the age at which the person lost all his hair, which is also referenced in the premise
if age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age in the premise, we can infer entailment
    label = "entailment"

print(label)

