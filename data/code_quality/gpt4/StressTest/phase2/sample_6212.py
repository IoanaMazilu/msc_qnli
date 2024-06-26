men_premise = 100
men_hypothesis = 200

# the hypothesis refers to the number of men employed by NHAI, also mentioned in the premise
if men_hypothesis != men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
