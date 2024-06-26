score_premise = [8, 2, 3]
score_hypothesis = [1, 2, 3]

# the hypothesis talks about the scores Mary got in the game, referenced also in the premise
if score_hypothesis[0] <= score_premise[0]:
    # check if the hypothesis value contradicts the estimate of less than'score_premise[0]'
    label = "contradiction"
elif score_hypothesis[1]!= score_premise[1]:
    # check if the hypothesis value contradicts the estimate of'score_premise[1]'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
