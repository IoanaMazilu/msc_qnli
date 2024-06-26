favor_war_percentage_premise = 52
opposition_percentage_premise = 46
majority_favor_war_percentage_hypothesis = 52

# the hypothesis mentions the percentage of those who favor the war, which is also mentioned in the premise
if majority_favor_war_percentage_hypothesis!= favor_war_percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif opposition_percentage_premise!= 46:
    # check if the percentage of opposition in the hypothesis contradicts the percentage of opposition in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
