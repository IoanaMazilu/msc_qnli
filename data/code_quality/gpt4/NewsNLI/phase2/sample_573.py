chelsea_goals_premise = 8
chelsea_goals_hypothesis = 8
villa_goals_premise = 0
villa_goals_hypothesis = 0

# the hypothesis mentions the score of Chelsea vs Aston Villa match, which is also mentioned in the premise
if chelsea_goals_hypothesis != chelsea_goals_premise:
    # check if the goals scored by Chelsea in the hypothesis contradict the goals scored by Chelsea in the premise
    label = "contradiction"
elif villa_goals_hypothesis != villa_goals_premise:
    # check if the goals scored by Aston Villa from the hypothesis contradicts the goals scored by Aston Villa in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
