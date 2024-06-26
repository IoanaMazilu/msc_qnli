men_to_women_ratio_premise = 6 / 6  # 1
men_to_women_ratio_hypothesis = 4 / 6  # 0.67

# the hypothesis refers to the ratio of men to women in the choir, which is also mentioned in the premise
if men_to_women_ratio_hypothesis > men_to_women_ratio_premise:
    # check if the hypothesis ratio contradicts the premise ratio
    label = "contradiction"
elif men_to_women_ratio_hypothesis == men_to_women_ratio_premise:
    # check if the hypothesis ratio is equal to the premise ratio
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio and is not equal to it, we can infer entailment
    label = "entailment"

print(label)
