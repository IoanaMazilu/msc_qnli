# Premise: The Saginaw News:Flag designer Bob Heft dies at 67.
# Hypothesis: Designer of 50-state U.S. flag dies at 67, Michigan paper reports.
# Golden Label: entailment

age_at_death_premise = 67
age_at_death_hypothesis = 67

# the hypothesis mentions the age at death of the flag designer, which is also referenced in the premise
if age_at_death_hypothesis != age_at_death_premise:
    # check if the age at death in the hypothesis contradicts the age at death reported in the premise
    label = "contradiction"
else:
    # if the age at death in the hypothesis does not contradict the age at death in the premise, we can infer entailment
    label = "entailment"

print(label)

