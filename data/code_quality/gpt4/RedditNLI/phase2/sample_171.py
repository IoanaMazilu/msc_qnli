year_premise = 1921
year_hypothesis = 1921

# the hypothesis and premise mention the year when the UK disposable income was comparably low
if year_hypothesis != year_premise:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis year is the same as the premise year, we can infer entailment
    label = "entailment"

print(label)
