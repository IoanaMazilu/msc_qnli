# Scores in premise
score_1_premise = 1
score_2_premise = 2
score_3_premise = 3
score_4_premise = 4
score_5_premise = 5

# Scores in hypothesis
score_1_hypothesis = 8
score_2_hypothesis = 2
score_3_hypothesis = 3
score_4_hypothesis = 4
score_5_hypothesis = 5

# Check if the scores in the hypothesis contradict the scores in the premise
if score_1_hypothesis <= score_1_premise or score_2_hypothesis!= score_2_premise or score_3_hypothesis!= score_3_premise or score_4_hypothesis!= score_4_premise or score_5_hypothesis!= score_5_premise:
    label = "contradiction"
else:
    # The premise gives only an estimate for the lowest score
    # Any score less than'score_1_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
