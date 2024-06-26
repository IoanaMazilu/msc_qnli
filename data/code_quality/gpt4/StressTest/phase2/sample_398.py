series_premise = 4
series_hypothesis = 3

# the hypothesis refers to the series problem mentioned in the premise
if series_hypothesis != series_premise:
    # check if the series problem in the hypothesis contradicts the series problem reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
