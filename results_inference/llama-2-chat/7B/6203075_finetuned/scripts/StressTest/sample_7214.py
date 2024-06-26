scores_premise = 1, 2, 3, 4, 5
scores_hypothesis = 1, 2, 3, 4, 5

# the hypothesis refers to the scores Roslin got in the game, which are also mentioned in the premise
if scores_hypothesis >= scores_premise:
    # check if the scores in the hypothesis contradict the scores in the premise
    label = "contradiction"
elif scores_hypothesis < scores_premise:
    # if the scores in the hypothesis are less than the scores in the premise, we can infer entailment
    label = "entailment"
else:
    # if the scores in the hypothesis are equal to the scores in the premise, we can infer neutrality
    label = "neutral"

print(label)
