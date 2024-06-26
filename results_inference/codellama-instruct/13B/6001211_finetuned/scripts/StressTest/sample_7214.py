# Scores in the premise and hypothesis
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [0, 2, 3, 4, 5]

# Check if the scores in the hypothesis contradict the scores in the premise
for score_h, score_p in zip(scores_hypothesis, scores_premise):
    if score_h >= score_p:
        label = "contradiction"
        break
else:
    # If the scores in the hypothesis do not contradict the scores in the premise,
    # we can infer entailment
    label = "entailment"

print(label)
