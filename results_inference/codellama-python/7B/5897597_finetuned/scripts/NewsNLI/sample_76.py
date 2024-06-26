favor_premise = 0.52
favor_hypothesis = 0.52

# the hypothesis mentions the percentage of people favoring the war in Afghanistan, which is also mentioned in the premise
if favor_hypothesis!= favor_premise:
    # check if the percentage in favor from the hypothesis contradicts the percentage in favor reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
