years_premise = 2
years_hypothesis = 2

# the hypothesis and premise mention the number of years since the last time a similar event occurred
if years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
