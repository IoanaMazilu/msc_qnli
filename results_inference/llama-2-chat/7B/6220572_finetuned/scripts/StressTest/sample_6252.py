scores_premise = [1, 2, 3, 4]
scores_hypothesis = [7, 2, 3, 4]

# the hypothesis refers to the scores in the premise
if scores_hypothesis[0] <= scores_premise[0]:
    # check if the hypothesis value contradicts the premise value of at least one score
    label = "contradiction"
elif scores_hypothesis[1]!= scores_premise[1]:
    # check if the hypothesis value contradicts the premise value of the second score
    label = "contradiction"
elif scores_hypothesis[2]!= scores_premise[2]:
    # check if the hypothesis value contradicts the premise value of the third score
    label = "contradiction"
elif scores_hypothesis[3]!= scores_premise[3]:
    # check if the hypothesis value contradicts the premise value of the fourth score
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
