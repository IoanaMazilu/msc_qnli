subject_scores_premise = [55, 67, 76, 82, 85]
subject_scores_hypothesis = [35, 67, 76, 82, 85]

# the hypothesis refers to the scores obtained by Reeya in different subjects, mentioned in the premise
if subject_scores_premise!= subject_scores_hypothesis:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
