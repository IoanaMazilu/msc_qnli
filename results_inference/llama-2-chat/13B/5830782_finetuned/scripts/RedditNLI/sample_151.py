drop_years_premise = 2
drop_years_hypothesis = 2

# the hypothesis and premise mention the time period of the biggest drop
if drop_years_hypothesis!= drop_years_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
