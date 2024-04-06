# Premise: Manchester City's designs on the English Premier League title were dealt an early blow as an injury time penalty from Darren Bent handed Sunderland a shock 1-0 win.
# Hypothesis: Sunderland beat Manchester City 1-0 at the Stadium of Light.
# Golden Label: neutral

man_city_goals_premise = 0
sunderland_goals_premise = 1
man_city_goals_hypothesis = 0
sunderland_goals_hypothesis = 1

# the hypothesis mentions the outcome of the soccer match, which is also mentioned in the premise
if man_city_goals_hypothesis != man_city_goals_premise:
    # check if the number of goals scored by Manchester City in the hypothesis contradicts the number of goals scored by Manchester City in the premise
    label = "contradiction"
elif sunderland_goals_hypothesis != sunderland_goals_premise:
    # check if the number of goals scored by Sunderland in the hypothesis contradicts the number of goals scored by Sunderland in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

