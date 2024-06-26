goals_scored_by_arsenal_premise = 4
goals_scored_by_galatasaray_premise = 1
goals_scored_by_arsenal_hypothesis = 4
goals_scored_by_galatasaray_hypothesis = 1
welbeck_goals_premise = 3
welbeck_goals_hypothesis = 3

# the hypothesis mentions the goal scores by both teams and the number of goals Welbeck scored, which are also mentioned in the premise
if goals_scored_by_arsenal_hypothesis != goals_scored_by_arsenal_premise:
    # check if the goals scored by Arsenal in the hypothesis contradicts the goals scored by Arsenal reported in the premise
    label = "contradiction"
elif goals_scored_by_galatasaray_hypothesis != goals_scored_by_galatasaray_premise:
    # check if the goals scored by Galatasaray from the hypothesis contradicts the goals scored by Galatasaray in the premise
    label = "contradiction"
elif welbeck_goals_hypothesis != welbeck_goals_premise:
    # check if the goals scored by Welbeck from the hypothesis contradicts the goals scored by Welbeck in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
