anil_age_premise = 7
son_age_premise = 3
anil_age_hypothesis = 1
son_age_hypothesis = 3

# the hypothesis refers to the ratio of the ages of Anil and his son mentioned in the premise
if anil_age_premise!= anil_age_hypothesis or son_age_premise!= son_age_hypothesis:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
