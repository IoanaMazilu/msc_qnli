anil_age_ratio_premise = 2/3
anil_age_ratio_hypothesis = 7/3

# the hypothesis refers to the ratio of Anil's age and his son's age mentioned in the premise
if anil_age_ratio_premise <= anil_age_ratio_hypothesis:
    # check if the estimate of 'anil_age_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
elif anil_age_ratio_hypothesis!= anil_age_ratio_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)