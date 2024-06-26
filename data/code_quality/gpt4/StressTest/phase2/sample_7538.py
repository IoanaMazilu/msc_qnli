subjects_scores_premise = [40, 60, 70, 80, 80]
subjects_scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the scores obtained by Reeya in different subjects mentioned in the premise
if any(score_hyp > score_prem for score_hyp, score_prem in zip(subjects_scores_hypothesis, subjects_scores_premise)):
    # check if any of the scores in the hypothesis contradicts the corresponding score in the premise
    label = "contradiction"
else:
    # if none of the scores in the hypothesis contradicts the corresponding score in the premise, we can infer entailment
    label = "entailment"

print(label)
