score_1_premise = 8
score_2_premise = 2
score_3_premise = 3
score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3

# the hypothesis talks about the scores Mary got in the game, referenced also in the premise
if score_1_hypothesis >= score_1_premise or score_2_hypothesis!= score_2_premise or score_3_hypothesis!= score_3_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any scores less than'score_1_premise','score_2_premise', and'score_3_premise' are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
