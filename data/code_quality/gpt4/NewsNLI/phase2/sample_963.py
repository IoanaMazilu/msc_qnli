age_at_death_premise = 95
age_at_death_hypothesis = 95

# the hypothesis mentions the age at which McPartland died, which is also mentioned in the premise
if age_at_death_hypothesis != age_at_death_premise:
    # check if the age at death in the hypothesis contradicts the age at death reported in the premise
    label = "contradiction"
else:
    # if the age at death in the hypothesis does not contradict the age at death in the premise, we can infer entailment
    label = "entailment"

print(label)
