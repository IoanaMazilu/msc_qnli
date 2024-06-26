patrick_michael_ratio_premise = 3/5
patrick_michael_ratio_hypothesis = 1/5
michael_monica_ratio_premise = 3/5
michael_monica_ratio_hypothesis = 3/5

# the hypothesis refers to the age ratios of Patrick to Michael and Michael to Monica, mentioned in the premise
if patrick_michael_ratio_hypothesis >= patrick_michael_ratio_premise:
    # check if the estimate of 'patrick_michael_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif michael_monica_ratio_hypothesis != michael_monica_ratio_premise:
    # check if the ratio of Michael to Monica in the hypothesis contradicts the same ratio reported in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
