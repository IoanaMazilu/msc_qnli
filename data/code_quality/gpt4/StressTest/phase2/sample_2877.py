years_ago_premise = 5
years_ago_hypothesis = 6
ratio_age_premise = 5
ratio_age_hypothesis = 5

# the hypothesis talks about the number of years ago Kate was a certain times as old as her son, both referenced in the premise
if years_ago_hypothesis < years_ago_premise:
    # check if the hypothesis value contradicts the number of years ago in the premise
    label = "contradiction"
elif ratio_age_hypothesis != ratio_age_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
