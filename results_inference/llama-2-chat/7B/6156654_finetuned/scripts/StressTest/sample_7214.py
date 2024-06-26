scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [less_than_1, 2, 3, 4, 5]

# the hypothesis talks about the scores Roslin got in the game, which are also mentioned in the premise
if scores_hypothesis[0] in scores_premise:
    # check if the first score in the hypothesis contradicts the premise
    label = "contradiction"
elif scores_hypothesis[1] in scores_premise and scores_hypothesis[1]!= scores_premise[1]:
    # check if the second score in the hypothesis contradicts the premise
    label = "contradiction"
elif scores_hypothesis[2] in scores_premise and scores_hypothesis[2]!= scores_premise[2]:
    # check if the third score in the hypothesis contradicts the premise
    label = "contradiction"
elif scores_hypothesis[3] in scores_premise and scores_hypothesis[3]!= scores_premise[3]:
    # check if the fourth score in the hypothesis contradicts the premise
    label = "contradiction"
elif scores_hypothesis[4] in scores_premise and scores_hypothesis[4]!= scores_premise[4]:
    # check if the fifth score in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
