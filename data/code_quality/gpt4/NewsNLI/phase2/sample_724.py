argentina_goals_premise = 2
greece_goals_premise = 0
south_korea_goals_premise = 2
nigeria_goals_premise = 2

south_korea_goals_hypothesis = 2
nigeria_goals_hypothesis = 2

# the hypothesis mentions the result of the South Korea vs Nigeria match, which is also mentioned in the premise
if south_korea_goals_hypothesis != south_korea_goals_premise or nigeria_goals_hypothesis != nigeria_goals_premise:
    # check if the scores in the hypothesis contradict the scores reported in the premise
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise scores, we can infer entailment
    label = "entailment"

print(label)
