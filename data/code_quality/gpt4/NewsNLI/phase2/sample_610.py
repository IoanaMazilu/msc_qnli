liverpool_goals_premise = 1
blackpool_goals_premise = 2
liverpool_goals_hypothesis = 1
blackpool_goals_hypothesis = 2

# the hypothesis mentions the result of the Liverpool vs Blackpool match, which is also mentioned in the premise
if liverpool_goals_hypothesis != liverpool_goals_premise:
    # check if the number of goals scored by Liverpool in the hypothesis contradicts the number of goals scored by Liverpool in the premise
    label = "contradiction"
elif blackpool_goals_hypothesis != blackpool_goals_premise:
    # check if the number of goals scored by Blackpool in the hypothesis contradicts the number of goals scored by Blackpool in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
