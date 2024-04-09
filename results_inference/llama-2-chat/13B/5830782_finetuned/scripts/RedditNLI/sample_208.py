year_premise = 1960
year_hypothesis = 1965

# the hypothesis and premise mention the year when home ownership reached its lowest level
if year_hypothesis < year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif year_hypothesis > year_premise:
    # check if the year in the hypothesis is greater than the year in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
