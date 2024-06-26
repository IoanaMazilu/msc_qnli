subjects_premise = [45, 67, 76, 82, 85]
subjects_hypothesis = [55, 67, 76, 82, 85]

# the hypothesis refers to the scores obtained by Reeya in different subjects, also mentioned in the premise
if subjects_hypothesis!= subjects_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
