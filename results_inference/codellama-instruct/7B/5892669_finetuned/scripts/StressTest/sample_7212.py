# defining the scores in the premise and hypothesis
scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [8, 2, 3, 4, 5]

# the hypothesis refers to the scores Roslin got in a game, which is also mentioned in the premise
# we compare the scores in the premise and hypothesis to check for contradictions
for score_premise, score_hypothesis in zip(scores_premise, scores_hypothesis):
    if score_premise >= score_hypothesis:
        # check if the score in the hypothesis contradicts the score in the premise
        label = "contradiction"
        break
else:
    # if the scores in the hypothesis do not contradict the scores in the premise, we can infer entailment
    label = "entailment"

print(label)
