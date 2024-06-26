# defining the scores in the premise and hypothesis
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [1, 2, 3, 4, 5]

# the hypothesis refers to the scores Roslin got in a game, mentioned in the premise
for score in scores_hypothesis:
    if score in scores_premise:
        # check if any score in the hypothesis contradicts the scores in the premise
        label = "contradiction"
        break
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
