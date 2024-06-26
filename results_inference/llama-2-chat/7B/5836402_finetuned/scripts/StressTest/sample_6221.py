priya_ratio_premise = 2
mani_ratio_premise = 4
rani_ratio_premise = 8

priya_ratio_hypothesis = 2
mani_ratio_hypothesis = 4
rani_ratio_hypothesis = 8

# the hypothesis refers to the ratio of money division between Priya, Mani and Rani mentioned in the premise
if priya_ratio_hypothesis >= priya_ratio_premise:
    # check if the estimate of 'priya_ratio_hypothesis' contradicts the ratio of money division in the premise
    label = "contradiction"
elif mani_ratio_hypothesis!= mani_ratio_premise or rani_ratio_hypothesis!= rani_ratio_premise:
    # check if the ratios of money division in the hypothesis contradict the ratios reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
