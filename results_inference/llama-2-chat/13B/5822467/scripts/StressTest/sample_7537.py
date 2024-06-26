subject_scores_premise = [50, 60, 70, 80, 80]
subject_scores_hypothesis = [40, 60, 70, 80, 80]

# calculate the average score for both the premise and the hypothesis
avg_premise = sum(subject_scores_premise) / len(subject_scores_premise)
avg_hypothesis = sum(subject_scores_hypothesis) / len(subject_scores_hypothesis)

# compare the averages to determine the label
if avg_premise > avg_hypothesis:
    label = "entailment"
elif avg_premise < avg_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
