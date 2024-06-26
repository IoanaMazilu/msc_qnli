# defining the scores in the premise and hypothesis
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [1, 2, 3, 4, 5]

# the hypothesis refers to the scores Roslin got in the game, which are also mentioned in the premise
for i in range(len(scores_premise)):
    if scores_hypothesis[i] >= scores_premise[i]:
        # check if the score in the hypothesis contradicts the score in the premise
        label = "contradiction"
        break
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
