men_women_ratio_premise = 4 / 7
men_women_ratio_hypothesis = 6 / 7

# the hypothesis refers to the ratio of men to women in the choir, also mentioned in the premise
if men_women_ratio_premise != men_women_ratio_hypothesis:
    # check if the ratio in the hypothesis contradicts the one stated in the premise
    label = "contradiction"
else:
    # if the ratios in the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)
