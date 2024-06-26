rajesh_age_premise = 20
mary_age_premise = 30
rajesh_age_hypothesis = 70
mary_age_hypothesis = 30

# the hypothesis refers to the ages of Rajesh and Mary mentioned in the premise
if rajesh_age_hypothesis < rajesh_age_premise:
    # check if 'rajesh_age_hypothesis' contradicts Rajesh's age in the premise
    label = "contradiction"
elif mary_age_hypothesis != mary_age_premise:
    # check if Mary's age in the hypothesis contradicts Mary's age in the premise
    label = "contradiction"
else:
    # if the hypothesis ages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
