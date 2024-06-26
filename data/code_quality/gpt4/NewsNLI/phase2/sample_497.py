barcelona_goals_premise = 2
real_madrid_goals_premise = 1
barcelona_goals_hypothesis = 2
real_madrid_goals_hypothesis = 1

# the hypothesis mentions the final score of the match, which is also mentioned in the premise
if barcelona_goals_hypothesis != barcelona_goals_premise:
    # check if the number of goals by Barcelona in the hypothesis contradicts the number of goals by Barcelona in the premise
    label = "contradiction"
elif real_madrid_goals_hypothesis != real_madrid_goals_premise:
    # check if the number of goals by Real Madrid in the hypothesis contradicts the number of goals by Real Madrid in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
