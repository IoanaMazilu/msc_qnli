favor_war_premise = 52
favor_war_hypothesis = 52

# the hypothesis mentions the percentage of people who favor the war in Afghanistan, which is also mentioned in the premise
if favor_war_hypothesis!= favor_war_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)