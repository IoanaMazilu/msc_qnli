subject_scores_premise = [40, 60, 70, 80, 80]
subject_scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the scores obtained by Reeya in different subjects, mentioned in the premise
if subject_scores_hypothesis[0] >= subject_scores_premise[0]:
    # check if the first score in the hypothesis contradicts the first score in the premise
    label = "contradiction"
elif subject_scores_hypothesis[1:4]!= subject_scores_premise[1:4]:
    # check if the scores in the other subjects in the hypothesis contradict the scores in the other subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
