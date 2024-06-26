# Scores in the premise and hypothesis
scores_premise = [7, 2, 3, 4]
scores_hypothesis = [1, 2, 3, 4]

# Check if any score in the hypothesis is greater than the corresponding score in the premise
for score_h, score_p in zip(scores_hypothesis, scores_premise):
    if score_h > score_p:
        label = "contradiction"
        break
else:
    # If all scores in the hypothesis are less than or equal to the corresponding scores in the premise,
    # then the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
