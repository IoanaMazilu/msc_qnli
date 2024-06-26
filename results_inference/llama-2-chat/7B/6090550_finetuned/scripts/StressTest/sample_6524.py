subjects_premise = [55, 67, 76, 82, 85]
subjects_hypothesis = [35, 67, 76, 82, 85]

# the hypothesis refers to the scores obtained by Reeya in different subjects, as mentioned in the premise

if subjects_hypothesis!= subjects_premise:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
