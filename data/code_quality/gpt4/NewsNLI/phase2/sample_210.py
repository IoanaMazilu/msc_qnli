manchester_goals_premise = 5
manchester_goals_hypothesis = 5
owen_goal_premise = 1
owen_goal_hypothesis = 1

# the hypothesis mentions Michael Owen's first goal for Manchester United and the 5-0 victory over Wigan, which are also mentioned in the premise
if manchester_goals_hypothesis != manchester_goals_premise:
    # check if the number of goals in the hypothesis contradicts the number of goals reported in the premise
    label = "contradiction"
elif owen_goal_hypothesis != owen_goal_premise:
    # check if the number of Owen's goals from the hypothesis contradicts the number of Owen's goals in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
