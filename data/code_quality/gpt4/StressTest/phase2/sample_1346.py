hitesh_age_premise = 40
ronnie_age_premise = 60
hitesh_age_hypothesis = 70
ronnie_age_hypothesis = 60

# the hypothesis refers to the ages of Hitesh and Ronnie mentioned in the premise
if hitesh_age_premise != hitesh_age_hypothesis:
    # check if the age of Hitesh in the hypothesis contradicts the age of Hitesh in the premise
    label = "contradiction"
elif ronnie_age_hypothesis != ronnie_age_premise:
    # check if the age of Ronnie in the hypothesis contradicts the age of Ronnie in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)