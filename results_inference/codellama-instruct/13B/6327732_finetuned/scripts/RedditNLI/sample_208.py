year_premise = 1960
year_hypothesis = 1965

# the hypothesis and premise mention the year when home ownership falls to the lowest level
if year_hypothesis!= year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis is the same as the year in the premise, we can infer entailment
    label = "entailment"

print(label)
