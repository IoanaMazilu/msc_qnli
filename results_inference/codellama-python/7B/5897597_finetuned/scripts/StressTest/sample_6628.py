score_1_premise = 8
score_2_premise = 2
score_3_premise = 3

score_1_hypothesis = 1
score_2_hypothesis = 2
score_3_hypothesis = 3

# the hypothesis refers to the scores Mary got in the game, which are also mentioned in the premise
if score_1_hypothesis >= score_1_premise:
    # check if the score in the hypothesis contradicts the premise of less than'score_1_premise'
    label = "contradiction"
elif score_2_hypothesis!= score_2_premise or score_3_hypothesis!= score_3_premise:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first score
    # any score less than'score_1_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
