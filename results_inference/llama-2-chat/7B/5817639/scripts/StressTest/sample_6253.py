score_premise = [7, 2, 3, 4]
score_hypothesis = [1, 2, 3, 4]

# the hypothesis talks about the scores obtained by Angel in the game
if score_hypothesis == score_premise:
    # if the hypothesis values are the same as the premise values, we can infer entailment
    label = "entailment"
elif any(score_hypothesis[i] > score_premise[i] for i in range(len(score_premise))):
    # if the hypothesis values are greater than the premise values in any position, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
