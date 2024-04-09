subject_scores_premise = [55, 67, 76, 82, 85]
subject_scores_hypothesis = [35, 67, 76, 82, 85]

# the hypothesis talks about the scores obtained by Reeya in different subjects, which are also mentioned in the premise
if subject_scores_hypothesis!= subject_scores_premise:
    # check if the scores in the hypothesis contradict the scores mentioned in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
