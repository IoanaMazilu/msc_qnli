# Premise: One year ago, the ratio of Roonie’s and Ronaldo’s age was 6:7 respectively.
# Hypothesis: One year ago, the ratio of Roonie’s and Ronaldo’s age was 5:7 respectively.
# Golden Label: contradiction

roonie_age_ratio_premise = 6
ronaldo_age_ratio_premise = 7
roonie_age_ratio_hypothesis = 5
ronaldo_age_ratio_hypothesis = 7

# the hypothesis refers to the age ratios of Roonie and Ronaldo one year ago, which are also mentioned in the premise
if roonie_age_ratio_hypothesis != roonie_age_ratio_premise:
    # check if the ratio of Roonie's age in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif ronaldo_age_ratio_hypothesis != ronaldo_age_ratio_premise:
    # check if the ratio of Ronaldo's age in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis ratios do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

