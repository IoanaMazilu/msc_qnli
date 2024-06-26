years_premise = 1960
years_hypothesis = 1965

# the hypothesis and premise mention the same period of time when home ownership fell to the lowest level
if years_hypothesis!= years_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)