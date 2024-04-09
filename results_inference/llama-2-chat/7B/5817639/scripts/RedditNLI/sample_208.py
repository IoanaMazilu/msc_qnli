lowest_level_premise = 1960
lowest_level_hypothesis = 1965

# check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
if lowest_level_hypothesis!= lowest_level_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
