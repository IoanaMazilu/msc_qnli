# Scores obtained by Reeya in different subjects as per the premise and hypothesis
scores_premise = [25, 67, 76, 82, 85]
scores_hypothesis = [65, 67, 76, 82, 85]

# Comparing each score from the hypothesis with the corresponding score from the premise
for score_premise, score_hypothesis in zip(scores_premise, scores_hypothesis):
    if score_hypothesis <= score_premise:
        # If any score from the hypothesis is less than or equal to the corresponding score from the premise, it contradicts the premise
        label = "contradiction"
        break
else:
    # If none of the scores from the hypothesis is less than the corresponding score from the premise, it is consistent with the premise
    # But it cannot be explicitly entailed from the premise as the premise does not specify the exact scores
    label = "neutral"

print(label)
