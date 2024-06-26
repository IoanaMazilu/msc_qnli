favor_war_premise = 0.52
favor_war_hypothesis = 0.52

# the hypothesis mentions the percentage of people who favor the war in Afghanistan, which is also mentioned in the premise
if favor_war_hypothesis != favor_war_premise:
    # check if the percentage of people favoring the war in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage from the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
