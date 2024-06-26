scores_premise = [1, 2, 3, 4]
scores_hypothesis = [less than 7, 2, 3, 4]

# the hypothesis refers to the scores mentioned in the premise
if scores_hypothesis[0] <= scores_premise[0]:
    # check if the estimate of'scores_hypothesis[0]' contradicts the score of'scores_premise[0]'
    label = "contradiction"
elif scores_hypothesis[1]!= scores_premise[1]:
    # check if the score of'scores_hypothesis[1]' contradicts the score of'scores_premise[1]'
    label = "contradiction"
elif scores_hypothesis[2]!= scores_premise[2]:
    # check if the score of'scores_hypothesis[2]' contradicts the score of'scores_premise[2]'
    label = "contradiction"
elif scores_hypothesis[3]!= scores_premise[3]:
    # check if the score of'scores_hypothesis[3]' contradicts the score of'scores_premise[3]'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
