# Scores from premise
score1_premise = 1
score2_premise = 2
score3_premise = 3
score4_premise = 4
score5_premise = 5

# Scores from hypothesis
score1_hypothesis = 8
score2_hypothesis = 2
score3_hypothesis = 3
score4_hypothesis = 4
score5_hypothesis = 5

# the hypothesis refers to the scores Roslin got in the game, as mentioned in the premise
if score1_hypothesis <= score1_premise:
    # check if the hypothesis value for score1 contradicts the premise
    label = "contradiction"
elif score2_hypothesis!= score2_premise:
    # check if the hypothesis value for score2 contradicts the premise
    label = "contradiction"
elif score3_hypothesis!= score3_premise:
    # check if the hypothesis value for score3 contradicts the premise
    label = "contradiction"
elif score4_hypothesis!= score4_premise:
    # check if the hypothesis value for score4 contradicts the premise
    label = "contradiction"
elif score5_hypothesis!= score5_premise:
    # check if the hypothesis value for score5 contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
