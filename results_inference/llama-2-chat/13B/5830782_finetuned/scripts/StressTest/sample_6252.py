# Scores in premise
score1_premise = 1
score2_premise = 2
score3_premise = 3
score4_premise = 4

# Scores in hypothesis
score1_hypothesis = 7
score2_hypothesis = 2
score3_hypothesis = 3
score4_hypothesis = 4

# the hypothesis talks about the scores Angel got in a game, referenced also in the premise
if score1_hypothesis <= score1_premise and score2_hypothesis == score2_premise and score3_hypothesis == score3_premise and score4_hypothesis == score4_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif score1_hypothesis > score1_premise or score2_hypothesis!= score2_premise or score3_hypothesis!= score3_premise or score4_hypothesis!= score4_premise:
    # check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
