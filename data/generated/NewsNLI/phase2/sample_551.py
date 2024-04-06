# Premise: Earlier, the United States came back from two goals behind to draw 2-2 with Slovenia in a pulsating encounter in Johannesburg.
# Hypothesis: Slovenia top the group after earlier 2-2 draw with the United States.
# Golden Label: neutral

us_goals_premise = 2
slovenia_goals_premise = 2
us_goals_hypothesis = 2
slovenia_goals_hypothesis = 2

# the hypothesis mentions the score of the game between the US and Slovenia, which is also mentioned in the premise
if us_goals_hypothesis != us_goals_premise:
    # check if the US score in the hypothesis contradicts the US score reported in the premise
    label = "contradiction"
elif slovenia_goals_hypothesis != slovenia_goals_premise:
    # check if the Slovenia score from the hypothesis contradicts the Slovenia score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we cannot infer entailment because the premise doesn't mention about Slovenia topping the group
    label = "neutral"

print(label)

