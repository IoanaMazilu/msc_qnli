score_one_premise = 1
score_one_hypothesis = 8

# the hypothesis talks about the minimum score of the game, referenced also in the premise
if score_one_hypothesis != score_one_premise:
    # check if the minimum score in the hypothesis contradicts the minimum score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
