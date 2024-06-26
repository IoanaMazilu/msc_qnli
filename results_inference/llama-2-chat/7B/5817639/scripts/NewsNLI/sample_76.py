favor_war_premise = 0.52
favor_war_hypothesis = 0.52

# the hypothesis mentions the same percentage of people supporting the war as in the premise
if favor_war_hypothesis == favor_war_premise:
    # if the values in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"
else:
    # if the values in the hypothesis contradict the values in the premise, we can infer contradiction
    label = "contradiction"

print(label)
