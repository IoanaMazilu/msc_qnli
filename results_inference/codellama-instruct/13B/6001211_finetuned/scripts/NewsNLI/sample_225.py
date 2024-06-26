score_premise = 5
score_hypothesis = 5
position_premise = 3
position_hypothesis = 3

# the hypothesis mentions the score of the game and Borussia Dortmund's new position in the table, which are also mentioned in the premise
if score_hypothesis!= score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif position_hypothesis!= position_premise:
    # check if the new position from the hypothesis contradicts the new position in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
