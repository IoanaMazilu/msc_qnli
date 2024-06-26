favor_premise = 0.52
favor_hypothesis = 0.52

# the hypothesis mentions the percentage of people who favor the war in Afghanistan, which is also mentioned in the premise
if favor_hypothesis!= favor_premise:
    # check if the percentage in favor of the war in the hypothesis contradicts the percentage in favor of the war in the premise
    label = "contradiction"
else:
    # if the percentage in favor of the war in the hypothesis does not contradict the percentage in favor of the war in the premise, we can infer entailment
    label = "entailment"

print(label)
