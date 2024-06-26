priya_ratio_premise = 2
mani_ratio_premise = 4
ravi_ratio_premise = 8

priya_ratio_hypothesis = 2
mani_ratio_hypothesis = 4
ravi_ratio_hypothesis = 8

# the hypothesis refers to the ratio of money distribution between Priya, Mani and Ravi mentioned in the premise
if priya_ratio_hypothesis >= priya_ratio_premise or mani_ratio_hypothesis >= mani_ratio_premise or ravi_ratio_hypothesis >= ravi_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
