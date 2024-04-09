anil_son_ratio_premise = 7 / 3
anil_son_ratio_hypothesis = 1 / 3

# the hypothesis talks about the ratio of Anil's and his son's ages, referenced also in the premise
if anil_son_ratio_hypothesis!= anil_son_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
