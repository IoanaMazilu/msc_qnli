subject_scores_premise = [65, 67, 76, 82, 85]
subject_scores_hypothesis = [85, 67, 76, 82, 85]

# the hypothesis talks about the scores obtained by Reeya in different subjects, referenced also in the premise
if sorted(subject_scores_premise) != sorted(subject_scores_hypothesis):
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the scores in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
