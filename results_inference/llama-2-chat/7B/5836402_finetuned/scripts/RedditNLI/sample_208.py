year_premise = 1960
year_hypothesis = 1965

# the hypothesis and premise mention the lowest level of home ownership in a certain year
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
