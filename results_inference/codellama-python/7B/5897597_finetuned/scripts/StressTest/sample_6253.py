score_1_premise = 7
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4

score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4

# the hypothesis refers to the scores Angel got in the game, which is also mentioned in the premise
if score_1_hypothesis >= score_1_premise:
    # check if the score in the hypothesis contradicts the premise of less than'score_1_premise'
    label = "contradiction"
elif score_2_hypothesis!= score_2_premise or score_3_hypothesis!= score_3_premise or score_4_hypothesis!= score_4_premise:
    # check if the scores in the hypothesis contradict the premise of'score_2_premise','score_3_premise', or'score_4_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the score of 1
    # any score of 1 less than'score_1_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
