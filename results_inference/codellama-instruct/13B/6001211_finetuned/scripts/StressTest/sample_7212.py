# Scores in the premise and hypothesis
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [less_than_8, 2, 3, 4, 5]

# Check if the scores in the hypothesis contradict the scores in the premise
for score_h, score_p in zip(scores_hypothesis, scores_premise):
    if score_h == less_than_8 and score_p == 1:
        # If the score in the hypothesis is less than 8 and the score in the premise is 1, it's a contradiction
        label = "contradiction"
    elif score_h!= score_p:
        # If the score in the hypothesis is not equal to the score in the premise, it's a contradiction
        label = "contradiction"

# If no contradiction was found, the relation is neutral
if label!= "contradiction":
    label = "neutral"

print(label)
