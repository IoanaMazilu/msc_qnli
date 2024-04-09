score_premise = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
score_hypothesis = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}

# the hypothesis talks about the scores gotten by Roslin in the game,
# referenced also in the premise
if score_hypothesis[1] <= score_premise[1]:
    # check if the hypothesis value contradicts the estimate of at least one score in the premise
    label = "contradiction"
elif score_hypothesis[2]!= score_premise[2]:
    # check if the number of scores in the hypothesis contradicts the number of scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
