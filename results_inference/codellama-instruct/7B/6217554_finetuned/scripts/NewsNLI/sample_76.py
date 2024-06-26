favor_premise = 52
favor_hypothesis = 52

# the hypothesis mentions the percentage of people who favor the war in Afghanistan, which is also referenced in the premise
if favor_hypothesis!= favor_premise:
    # check if the percentage of people who favor the war in Afghanistan from the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
