# Scores in the premise and hypothesis
score_premise = [1, 2, 3]
score_hypothesis = [0, 2, 3]

# Check if the scores in the hypothesis contradict the scores in the premise
for i in range(len(score_premise)):
    if score_hypothesis[i] >= score_premise[i]:
        label = "contradiction"
        break
else:
    # If the scores in the hypothesis do not contradict the scores in the premise,
    # but they do not fully entail them either
    label = "neutral"

print(label)
