favor_premise = 0.52
favor_hypothesis = 0.52
oppose_premise = 0.46

# the hypothesis mentions the percentage of people favoring the war, which is also mentioned in the premise
if favor_hypothesis!= favor_premise:
    # check if the percentage favoring the war in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
