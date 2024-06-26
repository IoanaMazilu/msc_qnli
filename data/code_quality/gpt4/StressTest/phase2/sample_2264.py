years_ago_premise = 8
years_ago_hypothesis = 8
older_ratio_premise = 12
older_ratio_hypothesis = 12

# the hypothesis relates to the same time frame and ratio of age mentioned in the premise
if older_ratio_hypothesis != older_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio mentioned in the premise
    label = "contradiction"
elif years_ago_hypothesis > years_ago_premise:
    # check if the number of years ago in the hypothesis contradicts the number of years ago mentioned in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
