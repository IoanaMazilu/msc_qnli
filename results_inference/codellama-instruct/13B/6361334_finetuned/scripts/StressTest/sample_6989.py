age_anil_premise = 7
age_son_premise = 3
age_anil_hypothesis = 1
age_son_hypothesis = 3

# the hypothesis refers to the ratio of the ages of Anil and his son at present, which is also mentioned in the premise
if age_anil_hypothesis!= age_anil_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif age_son_hypothesis!= age_son_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
