favor_war_premise = 52
favor_war_hypothesis = 52
opposition_premise = 46

# the hypothesis mentions the percentage of favor and opposition, which are also mentioned in the premise
if favor_war_hypothesis!= favor_war_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif opposition_premise!= 46:
    # check if the percentage of opposition in the hypothesis contradicts the percentage of opposition in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
