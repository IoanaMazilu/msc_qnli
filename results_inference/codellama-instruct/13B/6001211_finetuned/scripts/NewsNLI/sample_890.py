losses_premise = 11
games_premise = 21
score_hypothesis = 3.2

# the hypothesis mentions the score of the game and the fact that Celtic snapped a drought, which are not mentioned in the premise
# the premise only mentions the record of Celtic's losses and games without a win away from home, which are not referenced in the hypothesis
# there is no numerical information in the hypothesis that can be compared to the premise
label = "neutral"

print(label)
