anil_son_ratio_premise = 7 / 3
anil_son_ratio_hypothesis = 2 / 3

# the hypothesis talks about the same ratio of ages mentioned in the premise
if anil_son_ratio_hypothesis >= anil_son_ratio_premise:
    # check if the hypothesis value contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
