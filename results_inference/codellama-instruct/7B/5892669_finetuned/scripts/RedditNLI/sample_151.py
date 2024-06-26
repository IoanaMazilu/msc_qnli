years_drop_premise = 2
years_drop_hypothesis = 2

# the hypothesis and premise mention the number of years of the biggest drop in prices
if years_drop_hypothesis!= years_drop_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
