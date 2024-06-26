subject_scores_premise = [40, 60, 70, 80, 80]
subject_scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the subject scores mentioned in the premise
if subject_scores_hypothesis >= subject_scores_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
