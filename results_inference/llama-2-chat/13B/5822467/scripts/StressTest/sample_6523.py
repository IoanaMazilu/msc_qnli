subject_scores_premise = [45, 67, 76, 82, 85]
subject_scores_hypothesis = [55, 67, 76, 82, 85]

# define variables with representative names for the numerical entities in both inputs
subject_scores_premise_avg = sum(subject_scores_premise) / len(subject_scores_premise)
subject_scores_hypothesis_avg = sum(subject_scores_hypothesis) / len(subject_scores_hypothesis)

# compare the two averages
if subject_scores_hypothesis_avg > subject_scores_premise_avg:
    # the hypothesis suggests a higher average score than the premise
    label = "entailment"
elif subject_scores_hypothesis_avg <= subject_scores_premise_avg:
    # the hypothesis suggests a lower or equal average score than the premise
    label = "neutral"
else:
    # the hypothesis suggests a contradictory average score than the premise
    label = "contradiction"

print(label)
