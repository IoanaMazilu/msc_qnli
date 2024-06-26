# scores in the premise
score1_premise = 1
score2_premise = 2
score3_premise = 3

# scores in the hypothesis
score1_hypothesis = 1
score2_hypothesis = 2
score3_hypothesis = 3

# the hypothesis refers to the scores Mary got in the game, which are also mentioned in the premise
if score1_hypothesis >= score1_premise or score2_hypothesis >= score2_premise or score3_hypothesis >= score3_premise:
    # check if the hypothesis scores contradict the premise scores
    label = "contradiction"
elif score1_hypothesis < score1_premise or score2_hypothesis < score2_premise or score3_hypothesis < score3_premise:
    # check if the hypothesis scores are less than the premise scores
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
