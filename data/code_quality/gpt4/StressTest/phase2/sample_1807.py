subject_scores_premise = [85, 67, 76, 82, 55]
subject_scores_hypothesis = [55, 67, 76, 82, 55]

# we check each score from the hypothesis if it contradicts with the premise 
for score_h in subject_scores_hypothesis:
    if score_h >= max(subject_scores_premise):
        # if the score from hypothesis is greater than or equal to the maximum score from the premise, then it's a contradiction
        label = "contradiction"
        break
else:
    # else it's neutral as we don't have explicit scores to compare
    label = "neutral"

print(label)
