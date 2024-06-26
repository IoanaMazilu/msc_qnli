subject_scores_premise = [40, 60, 70, 80, 80]
subject_scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the scores obtained by Reeya in different subjects mentioned in the premise
if any(subject_score_hypothesis >= subject_score_premise for subject_score_hypothesis, subject_score_premise in zip(subject_scores_hypothesis, subject_scores_premise)):
    # check if any of the scores in the hypothesis contradicts the scores in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
