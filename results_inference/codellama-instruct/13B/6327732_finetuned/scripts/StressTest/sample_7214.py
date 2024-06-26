scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [0, 1, 2, 3, 4]

# the hypothesis talks about the scores in a game, referenced also in the premise
if scores_hypothesis[0]!= 0:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif scores_hypothesis[1]!= scores_premise[0]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif scores_hypothesis[2]!= scores_premise[1]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif scores_hypothesis[3]!= scores_premise[2]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif scores_hypothesis[4]!= scores_premise[3]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any number of scores greater than'scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
