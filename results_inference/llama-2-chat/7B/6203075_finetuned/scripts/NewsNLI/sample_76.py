favor_war_percentage_premise = 52
favor_war_percentage_hypothesis = 52
opposition_percentage_premise = 46

# the hypothesis mentions the percentage in favor of the war, which is also mentioned in the premise
if favor_war_percentage_hypothesis!= favor_war_percentage_premise:
    # check if the percentage in favor of the war in the hypothesis contradicts the percentage in favor of the war in the premise
    label = "contradiction"
elif opposition_percentage_hypothesis!= opposition_percentage_premise:
    # check if the percentage in opposition in the hypothesis contradicts the percentage in opposition in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
