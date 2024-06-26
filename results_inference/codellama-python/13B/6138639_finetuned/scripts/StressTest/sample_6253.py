score_1_premise = 7
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4

score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4

# the hypothesis talks about the scores Angel got in the game, referenced also in the premise
if score_1_hypothesis >= score_1_premise:
    # check if the hypothesis value contradicts the estimate of less than'score_1_premise'
    label = "contradiction"
elif score_2_hypothesis!= score_2_premise:
    # check if the score 2 in the hypothesis contradicts the score 2 reported in the premise
    label = "contradiction"
elif score_3_hypothesis!= score_3_premise:
    # check if the score 3 in the hypothesis contradicts the score 3 reported in the premise
    label = "contradiction"
elif score_4_hypothesis!= score_4_premise:
    # check if the score 4 in the hypothesis contradicts the score 4 reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any scores less than'score_1_premise' and equal to'score_2_premise','score_3_premise', and'score_4_premise' are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
