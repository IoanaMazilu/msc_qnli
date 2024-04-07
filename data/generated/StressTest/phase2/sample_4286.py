# Premise: Rajesh is 20 years old and Mary is 30 years old.
# Hypothesis: Rajesh is more than 20 years old and Mary is 30 years old.
# Golden Label: contradiction

rajesh_age_premise = 20
mary_age_premise = 30
rajesh_age_hypothesis = 20
mary_age_hypothesis = 30

# the hypothesis refers to the age of Rajesh and Mary mentioned in the premise
if rajesh_age_hypothesis != rajesh_age_premise:
    # check if the age of Rajesh in the hypothesis contradicts the age of Rajesh reported in the premise
    label = "contradiction"
elif mary_age_hypothesis != mary_age_premise:
    # check if the age of Mary in the hypothesis contradicts the age of Mary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

