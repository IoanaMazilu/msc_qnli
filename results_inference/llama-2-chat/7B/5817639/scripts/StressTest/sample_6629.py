score_premise = [1, 2, 3]
score_hypothesis = [less_than_1, less_than_2, less_than_3]

# the hypothesis refers to the scores Mary got in the game, as mentioned in the premise
if score_hypothesis[0] <= score_premise[0]:
    # check if the estimate of'score_hypothesis[0]' contradicts the number of scores Mary got in the premise
    label = "contradiction"
elif score_hypothesis[1] <= score_premise[1]:
    # check if the estimate of'score_hypothesis[1]' contradicts the number of scores Mary got in the premise
    label = "contradiction"
elif score_hypothesis[2] <= score_premise[2]:
    # check if the estimate of'score_hypothesis[2]' contradicts the number of scores Mary got in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
