# defining the variables for the premise and hypothesis
scores_premise = [1, 2, 3, 4]
scores_hypothesis = [7, 2, 3, 4]

# the hypothesis refers to the scores Angel got in the game, mentioned in the premise
if scores_hypothesis[0] < scores_premise[0]:
    # check if the first score in the hypothesis contradicts the first score in the premise
    label = "contradiction"
elif scores_hypothesis[1:]!= scores_premise[1:]:
    # check if the remaining scores in the hypothesis contradict the remaining scores in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
