sentsimple_premise = 1
sentsimple_hypothesis = 1

# the hypothesis mentions the number of attack helicopters, which is also mentioned in the premise
if sentsimple_hypothesis!= sentsimple_premise:
    # check if the number of helicopters in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
