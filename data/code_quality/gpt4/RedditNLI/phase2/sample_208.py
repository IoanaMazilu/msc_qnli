year_premise = 1960
year_hypothesis = 1965

# the hypothesis and premise mention the year of the lowest level of home ownership
if year_hypothesis > year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif year_hypothesis < year_premise:
    # check if the year in the hypothesis is earlier than the year in the premise
    label = "contradiction"
else:
    # if the year in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
